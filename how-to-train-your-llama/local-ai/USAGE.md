# Getting Started
Clone the repository and navigate to the `local-ai` directory:
```bash
git clone https://github.com/skisec/cackalacky-ai-village.git && \
cd cackalacky-ai-village/how-to-train-your-llama/local-ai
```

---
## Table of Contents
- [Deployment Modes](#deployment-modes)
  - [CPU Only](#cpu-only)
  - [NVIDIA GPU](#nvidia-gpu)
  - [AMD GPU](#amd-gpu)
    - [Windows](#amd-on-windows)
    - [Linux](#amd-on-linux)
  - [Apple Silicon](#apple-silicon)
- [Downloading Models](#downloading-models)
  - [Using Ollama](#using-ollama)
  - [Using Ollama Docker](#using-ollama-docker)
  - [Using HuggingFace](#using-huggingface)
  - [Using OpenWebUI](#using-openwebui)
- [Stopping Services](#stopping-the-services)
- [Troubleshooting](#troubleshooting)

## Deployment Modes
Depending on your hardware setup, you can use one of the pre-defined docker profiles to spin up the services.
---

### CPU Only
```bash
docker compose --profile cpu up -d
```

### NVIDIA GPU

> [!NOTE]
> For more guidance, please see
> [Ollama Docker instructions](https://github.com/ollama/ollama/blob/main/docs/docker.md).

```bash
docker compose --profile gpu-nvidia up -d
```
### AMD GPU

#### AMD on Windows
Install Ollama directly on your Windows system.
For more guidance, please see [Ollama Windows](https://github.com/ollama/ollama/blob/main/docs/windows.md)
```powershell
docker compose --profile gpu-amd-win up -d
```

#### AMD on Linux
```bash
docker compose --profile gpu-amd-linux up -d
```

> [!NOTE]
> You may need to configure LLVM overrides to get ROCm to work with Ollama. For more guidance, please see
> [Ollama GPU Overrides on Linux](https://github.com/ollama/ollama/blob/main/docs/gpu.md#overrides-on-linux)

### Apple Silicon
While Ollama supports GPU acceleration on Apple Silicon via the Metal API, Docker cannot access the GPU/Neural Engine. For the best performance, it is recommended to run Ollama directly on your Mac

You can run Ollama on your Mac with one of the options below:
 - [Download Ollama](https://ollama.com/download/mac)
 - Install via homebrew - `brew install ollama`

```bash
docker compose --profile macos up -d
```

## Accessing Services

*   **OpenWebUI**: Open your web browser and go to `http://localhost:8080`.
*   **Ollama API**: `http://localhost:11434`

## Downloading models

You can download models in a few different ways.

### Using Ollama

```bash
ollama pull <model_name>
```

### Using Ollama Docker

```bash
docker exec -it ollama ollama pull <model_name>
```

### Using OpenWebUI

Navigate to the OpenWebUI interface and use the model browser to download models.

### Using Huggingface

See details here: [Huggingface Ollama](https://huggingface.co/docs/hub/en/ollama)

## Stopping the Services

To stop the running containers:

```bash
docker compose --profile "*" down
```

## Troubleshooting

*   **Ollama Troubleshooting:** See [Ollama Troubleshooting](https://github.com/ollama/ollama/blob/main/docs/troubleshooting.md)
*   **Open-WebUI Troubleshooting:** See [Open-WebUI Troubleshooting](https://docs.openwebui.com/troubleshooting/)
*   **Port Conflicts:** If `8080` or `11434` are in use, edit the `ports` section in `docker-compose.yaml` for the relevant service(s).