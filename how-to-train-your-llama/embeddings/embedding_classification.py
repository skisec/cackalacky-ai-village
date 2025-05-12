import requests
import json
import numpy as np
import gradio as gr
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict, Tuple

# Configuration
OLLAMA_BASE_URL = "http://localhost:11434"  # Default Ollama API endpoint
DEFAULT_EMBEDDING_MODEL = "nomic-embed-text"


class EmbeddingClassifier:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.categories = {}
        self.category_embeddings = {}

    def add_category(self, category_name: str, examples: List[str]):
        """Add or update a category with example texts"""
        self.categories[category_name] = examples
        embeddings = [self.get_embedding(text) for text in examples]
        valid_embeddings = [e for e in embeddings if len(e) > 0]
        if valid_embeddings:
            self.category_embeddings[category_name] = np.mean(valid_embeddings, axis=0)
            return True
        return False

    def get_embedding(self, text: str) -> np.ndarray:
        """Get the embedding vector for a text using Ollama API"""
        url = f"{OLLAMA_BASE_URL}/api/embeddings"
        payload = {"model": self.model_name, "prompt": text}

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            embedding = np.array(response.json()["embedding"])
            return embedding
        except Exception as e:
            print(f"Error getting embedding: {e}")
            return np.array([])

    def classify(self, text: str) -> List[Tuple[str, float]]:
        """
        Classify text against all categories.

        Returns:
            List of (category_name, confidence_score) tuples, sorted by confidence
        """
        # Get embedding for the input text
        text_embedding = self.get_embedding(text)

        if len(text_embedding) == 0 or not self.category_embeddings:
            return [("No valid categories or embedding failed", 0.0)]

        # Calculate similarity to each category
        results = []
        for category, category_embedding in self.category_embeddings.items():
            similarity = cosine_similarity([text_embedding], [category_embedding])[0][0]
            results.append((category, similarity))

        # Sort by similarity score (descending)
        return sorted(results, key=lambda x: x[1], reverse=True)


# Function to get available Ollama models
def get_available_models():
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags")
        models = [model["name"] for model in response.json().get("models", [])]
        # Filter for embedding models - this is approximate as Ollama doesn't explicitly mark them
        embedding_models = [
            m
            for m in models
            if any(
                term in m.lower()
                for term in ["embed", "minilm", "e5", "nomic", "bert", "sentence"]
            )
        ]
        return embedding_models or [DEFAULT_EMBEDDING_MODEL]
    except:
        return [DEFAULT_EMBEDDING_MODEL]


# Create a Gradio interface for the classifier
def create_ui():
    embedding_models = get_available_models()
    classifier = EmbeddingClassifier(
        embedding_models[0] if embedding_models else DEFAULT_EMBEDDING_MODEL
    )

    with gr.Blocks(title="Ollama Embedding Classifier") as app:
        gr.Markdown("# Text Classification with Ollama Embeddings")

        with gr.Row():
            with gr.Column(scale=1):
                model_dropdown = gr.Dropdown(
                    embedding_models,
                    label="Embedding Model",
                    value=(
                        embedding_models[0]
                        if embedding_models
                        else DEFAULT_EMBEDDING_MODEL
                    ),
                    info="Select an embedding model from your Ollama installation",
                )

                gr.Markdown("## Define Categories")
                category_name = gr.Textbox(label="Category Name")
                category_examples = gr.TextArea(
                    label="Examples (one per line)",
                    placeholder="Enter example texts, one per line",
                )
                add_btn = gr.Button("Add Category")

                categories_display = gr.Dataframe(
                    headers=["Category", "Number of Examples"],
                    datatype=["str", "number"],
                    label="Defined Categories",
                )

            with gr.Column(scale=1):
                gr.Markdown("## Test Classification")
                test_text = gr.TextArea(label="Text to Classify")
                classify_btn = gr.Button("Classify")

                results_display = gr.Dataframe(
                    headers=["Category", "Confidence"],
                    datatype=["str", "number"],
                    label="Classification Results",
                )

        # State variables to track categories
        category_state = gr.State({})

        # Update model when dropdown changes
        def update_model(model_name):
            nonlocal classifier
            classifier = EmbeddingClassifier(model_name)
            return {}  # Reset categories

        model_dropdown.change(
            update_model, inputs=[model_dropdown], outputs=[category_state]
        )

        # Add category handler
        def add_category(name, examples_text, categories):
            if not name.strip():
                return categories, [[f"Error: Category name required", 0]]

            examples = [
                ex.strip() for ex in examples_text.strip().split("\n") if ex.strip()
            ]
            if not examples:
                return categories, [[f"Error: No valid examples provided", 0]]

            # Update classifier
            classifier.add_category(name, examples)

            # Update state
            categories[name] = examples

            # Update display
            categories_display_data = [
                [cat, len(exs)] for cat, exs in categories.items()
            ]

            return categories, categories_display_data

        add_btn.click(
            add_category,
            inputs=[category_name, category_examples, category_state],
            outputs=[category_state, categories_display],
        )

        # Classification handler
        def classify_text(text, categories):
            if not text.strip():
                return [[f"Error: No text to classify", 0]]

            if not categories:
                return [[f"Error: No categories defined", 0]]

            # Ensure classifier has all categories
            for cat, examples in categories.items():
                if cat not in classifier.categories:
                    classifier.add_category(cat, examples)

            results = classifier.classify(text)
            return [[cat, float(conf)] for cat, conf in results]

        classify_btn.click(
            classify_text, inputs=[test_text, category_state], outputs=[results_display]
        )

    return app


if __name__ == "__main__":
    # Check if Ollama is running
    try:
        requests.get(f"{OLLAMA_BASE_URL}/api/version")
        print("Connected to Ollama API successfully.")

        # Launch the Gradio interface
        app = create_ui()
        app.launch()

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Ollama API.")
        print("Make sure Ollama is running on your system with: 'ollama serve'")
