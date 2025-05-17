# How to Fleece Your Llama: Evaluating LLMs with Promptfoo

This repository showcases the use of Promptfoo, an open-source command-line tool designed for evaluating and red-teaming Large Language Models (LLMs) and LLM-enabled applications.

## Table of Contents

- [How to Fleece Your Llama: Evaluating LLMs with Promptfoo](#how-to-fleece-your-llama-evaluating-llms-with-promptfoo)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
    - [What is Promptfoo?](#what-is-promptfoo)
    - [What Can You Evaluate?](#what-can-you-evaluate)
  - [Prerequisites](#prerequisites)
  - [Setup and Usage](#setup-and-usage)
    - [Installation](#installation)
      - [Command-Line Usage](#command-line-usage)
      - [Self-Hosted Docker Server](#self-hosted-docker-server)
    - [Running Evaluation Examples](#running-evaluation-examples)
      - [General Notes on Examples](#general-notes-on-examples)
      - [Bias Evaluation](#bias-evaluation)
      - [Factuality Evaluation](#factuality-evaluation)
      - [Red Teaming Evaluation](#red-teaming-evaluation)
  - [Test Findings & Observations](#test-findings--observations)
    - [Summary of Findings](#summary-of-findings)
    - [Key Observations](#key-observations)
  - [Directory Contents](#directory-contents)
  - [Official Documentation & Further Resources](#official-documentation--further-resources)
    - [Official Tool Documentation](#official-tool-documentation)
    - [Additional Promptfoo Resources](#additional-promptfoo-resources)

## Overview

### What is Promptfoo?
Promptfoo is an open-source command-line tool designed for evaluating and red-teaming Large Language Models (LLMs) and LLM-enabled applications. It helps you systematically test your prompts, models, and configurations to ensure quality, safety, and reliability.


## Prerequisites

To run the examples in this repository, you will need:
- [Ollama](https://ollama.com/) (for serving the models to be tested)
- [Node.js 18 or newer](https://nodejs.org/en/download/) (for running Promptfoo CLI)
- [Docker](https://docs.docker.com/get-started/get-docker/) (optional, for sharing and storing evaluation results)

## Setup and Usage

### Installation

Follow the official Promptfoo guides for installation:

#### Command-Line Usage
For using Promptfoo directly from your command line, see the [Promptfoo Installation Guide](https://www.promptfoo.dev/docs/installation/).

#### Self-Hosted Docker Server
If you prefer to run Promptfoo as a self-hosted service (e.g., for sharing results), see the [Promptfoo Self-Hosting Guide](https://www.promptfoo.dev/docs/usage/self-hosting/).

### Running Evaluation Examples

This repository contains sample test use cases in the `examples` directory, configured to run against models hosted locally via Ollama. These can be adapted to run against a variety of other LLM providers supported by Promptfoo.

More examples can be found in Promptfoo's [official documentation](https://www.promptfoo.dev/docs/category/guides/) or [GitHub repository](https://github.com/promptfoo/promptfoo/tree/main/examples).

#### General Notes on Examples
Each of the example test cases below are configured to use the following Ollama Models by default (you can change these in the respective `promptfooconfig.yaml` files):
- `gemma3:4b-it-qat`
- `phi4-mini:latest`
- `llama3.2:3b`
- `qwen3:4b`

#### Bias Evaluation
This test case, located in `examples/bias/`, evaluates for potential political and religious biases. The plugins used are:
- `politics`: This plugin helps identify potential vulnerabilities where the AI might inadvertently take political stances or engage in politically sensitive discussions. ([Plugin details](https://www.promptfoo.dev/docs/red-team/plugins/politics/))
- `religion`: This plugin tests whether the AI can express biases, make insensitive comments, or engage in inappropriate discussions related to religion. ([Plugin details](https://www.promptfoo.dev/docs/red-team/plugins/religion/))

**Running the Bias example:**
Navigate to the `examples/bias` directory and run:
```bash
npx promptfoo@latest redteam run
```
To view the results locally:
```bash
npx promptfoo@latest view
```
If running the self-hosted docker container, you can share and view the results by running:
```bash
export PROMPTFOO_REMOTE_API_BASE_URL=http://your-server-address:3000
export PROMPTFOO_REMOTE_APP_BASE_URL=http://your-server-address:3000
npx promptfoo@latest share
```

#### Factuality Evaluation
This test case, located in `examples/factuality/`, is an adaptation of the [factuality evaluation](https://www.promptfoo.dev/docs/guides/factuality-eval/) example from Promptfoo's documentation.
Factuality is the measure of how accurately an LLM's response aligns with established facts or reference information.

**Running the Factuality example:**
Navigate to the `examples/factuality` directory and run:
```bash
npx promptfoo@latest eval
```
To view the results locally:
```bash
npx promptfoo@latest view
```
If running the self-hosted docker container, you can share and view the results by running:
```bash
export PROMPTFOO_REMOTE_API_BASE_URL=http://your-server-address:3000
export PROMPTFOO_REMOTE_APP_BASE_URL=http://your-server-address:3000
npx promptfoo@latest share
```

#### Red Teaming Evaluation
This test case, located in `examples/redteam/`, is an example of [red teaming](https://www.promptfoo.dev/docs/red-team/). The example uses a small set of red team plugins to evaluate the security and safety of the Ollama models.

**Running the Red Teaming example:**
Navigate to the `examples/redteam` directory and run:
```bash
npx promptfoo@latest redteam run
```
To view the results locally:
```bash
npx promptfoo@latest view
```
If running the self-hosted docker container, you can share and view the results by running:
```bash
export PROMPTFOO_REMOTE_API_BASE_URL=http://your-server-address:3000
export PROMPTFOO_REMOTE_APP_BASE_URL=http://your-server-address:3000
npx promptfoo@latest share
```

## Test Findings & Observations

### Summary of Findings
The raw CSV and JSON results of the tests performed for this repository are available in the `findings` directory.

Below is a summary of these findings:

**Bias**
| Model            | Passing Score | Total Tests | # Passed |
| ---------------- | ------ | ----------- | ------ |
| gemma3:4b-it-qat | 58.10% | 105         | 61     |
| phi4-mini:latest | 69.52% | 105         | 73     |
| llama3.2:3b      | 81.90% | 105         | 86     |
| qwen3:4b         | 59.05% | 105         | 62     |

**Factuality**
| Model            | Passing Score | Total Tests | # Passed |
| ---------------- | ----- | ----------- | ------ |
| gemma3:4b-it-qat | 71%   | 100         | 71     |
| phi4-mini:latest | 83%   | 100         | 83     |
| llama3.2:3b      | 83%   | 100         | 83     |
| qwen3:4b         | 83%   | 100         | 83     |

**Red Team**
| Model | Passing Score | Total Tests | # Passed |
| ---------------- | ----- | ----------- | ------ |
| gemma3:4b-it-qat | 57.23%   | 650         | 372    |
| phi4-mini:latest | 69.54% | 650         | 452    |
| llama3.2:3b      | 76.62% | 650         | 498    |
| qwen3:4b         | 60.15% | 650         | 391    |

### Key Observations
When initially testing some examples that are more 'comprehensive', it was taking an extremely long time for the tests to run, with some taking more than 12 hours.

For simplicity, these examples were set up using a relatively minimal configuration and limited number of plugins, strategies, and test cases. Due to this, there was a tradeoff in test accuracy which may lead to false positives in the test results.

Despite this, the results do provide valuable insights into the quality and security of the models used in the tests. Upon reviewing the results of the various tests, it was found that there were some tests marked as 'failed' that could be considered false positives with further refinement of assertions or prompts.

With a more comprehensive test setup, it is possible to reduce the number of false positives and improve the accuracy of the test results. Details around preventing false positives can be found in the Promptfoo documentation: [Troubleshooting False Positives](https://www.promptfoo.dev/docs/red-team/troubleshooting/false-positives/).

## Directory Contents
*   `README.md`: This file.
*   `examples/`: Contains subdirectories for `bias`, `factuality`, and `redteam` evaluations. Each subdirectory includes a `promptfooconfig.yaml` and other necessary files for the tests.
*   `findings/`: Contains raw CSV and JSON results from the example test runs performed for this repository.

## Official Documentation & Further Resources

### Official Tool Documentation
*   **Promptfoo:** [https://www.promptfoo.dev/docs/](https://www.promptfoo.dev/docs/)
*   **Ollama:** [https://github.com/ollama/ollama/tree/main/docs](https://github.com/ollama/ollama/tree/main/docs)

### Additional Promptfoo Resources
*   **Promptfoo Guides:** [https://www.promptfoo.dev/docs/category/guides/](https://www.promptfoo.dev/docs/category/guides/)
*   **Promptfoo GitHub Examples:** [https://github.com/promptfoo/promptfoo/tree/main/examples](https://github.com/promptfoo/promptfoo/tree/main/examples)