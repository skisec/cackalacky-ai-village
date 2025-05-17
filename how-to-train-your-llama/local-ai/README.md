# How to Train Your Llama: Local AI with Ollama & OpenWebUI

This guide explains how to set up **Ollama** (a tool for running large language models) and **OpenWebUI** (a web interface for AI models) locally using Docker Compose. It covers hardware considerations, software prerequisites, and step-by-step instructions for various deployment modes.

## Table of Contents
- [How to Train Your Llama: Local AI with Ollama & OpenWebUI](#how-to-train-your-llama-local-ai-with-ollama--openwebui)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
    - [What is Ollama?](#what-is-ollama)
    - [What is OpenWebUI?](#what-is-openwebui)
    - [Understanding Ollama Quantization](#understanding-ollama-quantization)
    - [Understanding Quantization Types](#understanding-quantization-types)
    - [Why Run LLMs Locally?](#why-run-llms-locally)
  - [Prerequisites](#prerequisites)
    - [Hardware Requirements](#hardware-requirements)
      - [GPU Requirements](#gpu-requirements)
    - [Software Requirements](#software-requirements)
  - [Setup and Usage](#setup-and-usage)
    - [1. Initial Setup (Clone Repository)](#1-initial-setup-clone-repository)
    - [2. Deployment Modes](#2-deployment-modes)
      - [CPU Only](#cpu-only)
      - [NVIDIA GPU](#nvidia-gpu)
      - [AMD GPU](#amd-gpu)
        - [AMD on Windows](#amd-on-windows)
        - [AMD on Linux](#amd-on-linux)
      - [Apple Silicon](#apple-silicon)
    - [3. Accessing Services](#3-accessing-services)
    - [4. Downloading Models](#4-downloading-models)
      - [Using Ollama CLI](#using-ollama-cli)
      - [Using Ollama Docker Command](#using-ollama-docker-command)
      - [Using OpenWebUI Interface](#using-openwebui-interface)
      - [Using Hugging Face](#using-hugging-face)
    - [5. Stopping Services](#5-stopping-services)
  - [Directory Contents](#directory-contents)
  - [Official Documentation & Further Resources](#official-documentation--further-resources)
    - [Official Tool Documentation](#official-tool-documentation)
    - [Troubleshooting](#troubleshooting)

## Overview

This guide will walk you through setting up a local environment for running Large Language Models (LLMs) using Ollama and interacting with them through OpenWebUI.

### What is Ollama?
Ollama is a tool that simplifies running open-source large language models locally. It packages models and provides an API for interaction, making it easier to get started with LLMs on your own hardware.

### What is OpenWebUI?
OpenWebUI is a user-friendly, extensible web interface for interacting with various LLMs, including those served by Ollama. It provides a chat interface, model management capabilities, RAG (Retrieval Augmented Generation) features, and more.

### Understanding Ollama Quantization

Model quantization is a process that reduces the precision of the numbers used to represent a model's weights, which can significantly decrease the model's size and improve inference speed, often with a manageable trade-off in performance. Ollama supports various quantization methods, each offering different balances between size, speed, and quality.

| Quant Type | Description                               | Notes                                         |
|------------|-------------------------------------------|-----------------------------------------------|
| **Old Quant Types (Legacy)** |||
| `Q4_0`     | Small, very high quality loss             | Legacy, prefer using `Q3_K_M`                 |
| `Q4_1`     | Small, substantial quality loss           | Legacy, prefer using `Q3_K_L`                 |
| `Q5_0`     | Medium, balanced quality                  | Legacy, prefer using `Q4_K_M`                 |
| `Q5_1`     | Medium, low quality loss                  | Legacy, prefer using `Q5_K_M`                 |
| **New Quant Types** |||
| `Q2_K`     | Smallest, extreme quality loss            | Not recommended                               |
| `Q3_K`     | (Alias for `Q3_K_M`) Very small, very high quality loss | Alias for `Q3_K_M`                            |
| `Q3_K_S`   | Very small, very high quality loss        |                                               |
| `Q3_K_M`   | Very small, very high quality loss        |                                               |
| `Q3_K_L`   | Small, substantial quality loss           |                                               |
| `Q4_K`     | (Alias for `Q4_K_M`) Medium, balanced quality | Alias for `Q4_K_M`                            |
| `Q4_K_S`   | Small, significant quality loss           |                                               |
| `Q4_K_M`   | Medium, balanced quality                  | **Recommended**                               |
| `Q5_K`     | (Alias for `Q5_K_M`) Large, very low quality loss | Alias for `Q5_K_M`                            |
| `Q5_K_S`   | Large, low quality loss                   | **Recommended**                               |
| `Q5_K_M`   | Large, very low quality loss              | **Recommended**                               |
| `Q6_K`     | Very large, extremely low quality loss    |                                               |
| `Q8_0`     | Very large, extremely low quality loss    | Not recommended                               |
| `F16`      | Extremely large, virtually no quality loss| Not recommended                               |
| `F32`      | Absolutely huge, lossless                 | Not recommended                               |

### Understanding Quantization Types

Quantization is a process that reduces the precision of the numbers used to represent a model's weights, which can significantly decrease the model's size and improve inference speed, often with a manageable trade-off in performance.

For more information about quantization methods, see the [Hugging Face documentation](https://huggingface.co/docs/transformers/quantization).

Here are some popular quantization methods:

* [GGUF](https://huggingface.co/docs/transformers/main/en/gguf)
* [GPTQ](https://huggingface.co/docs/transformers/main/en/quantization/gptq)
* [AWQ](https://huggingface.co/docs/transformers/main/en/quantization/awq)

### Why Run LLMs Locally?
Running LLMs locally offers several advantages:
*   **Data Privacy:** Your data and prompts do not leave your machine, ensuring confidentiality.
*   **Cost Savings:** Avoid API fees associated with cloud-hosted models.
*   **Offline Accessibility:** Use models without needing an active internet connection (after initial download).
*   **Customization & Control:** Greater control over model selection, configuration, and experimentation.

## Prerequisites

### Hardware Requirements

For decent results, the minimum requirements are:
- **CPU:** >4 cores
- **RAM:** >8GB
- **Storage:** >50GB

For optimal performance, it's highly recommended to use a GPU with this setup. CPU inference is **painfully** slow.

#### GPU Requirements
The table below shows a breakdown of the VRAM, example GPUs and model sizes that can be *comfortably* run. This is just a general reference, as your mileage may vary depending on CPU and RAM.

| VRAM Size | GPUs | Max Model Sizes |
| --- | --- | --- |
| 6GB | **NVIDIA**: RTX 1060, 1660, 2060, 3060, 4050 <br> **AMD**: 5600 XT, 7500 XT| 7B |
| 8GB | **NVIDIA**: RTX 2060 Super, 2070 Super, 2080 Super, 3060 Ti, 3070, 4060 <br> **AMD**: Radeon RX 5700, 5700 XT, 6600 XT, 7600 | 8B |
| 12GB | **NVIDIA**: RTX 2060, 3060, 3080, 4070, 4080 <br> **AMD**: Radeon RX 6700 XT, 7700 XT | 14B |
| 16GB | **NVIDIA**: RTX 3070 Ti, 4070 Ti, 4080, 4090 <br> **AMD**: Radeon RX 5700 XT, 6800 XT, 6900 XT, 6900 XTX, 7600 XT, 7800 XT | 14B |
| 20GB | **NVIDIA**: RTX 3090, 3090 Ti, 4090,  <br> **AMD**: Radeon RX 7900 XT, 7950 XT | 24B |
| 24GB | **NVIDIA**: RTX 4090 Ti <br> **AMD**: Radeon RX 7900 XTX, 7950 XTX, 7990 XTX | 32B |

Ollama also supports Apple Silicon through the Metal API. The same general guidance can be applied, based on the amount of memory your Mac has.

### Software Requirements

- [Docker](https://docs.docker.com/get-started/get-docker/)

*For NVIDIA GPUs*
- [NVIDIA Drivers](https://www.nvidia.com/Download/index.aspx)
- [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)

*For AMD GPUs*
- [ROCm Drivers](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/)

## Setup and Usage

### 1. Initial Setup (Clone Repository)
Clone the repository and navigate to the `local-ai` directory:
```bash
git clone https://github.com/skisec/cackalacky-ai-village.git && \
cd cackalacky-ai-village/how-to-train-your-llama/local-ai
```

### 2. Deployment Modes
Depending on your hardware setup, you can use one of the pre-defined docker profiles to spin up the services.

#### CPU Only
```bash
docker compose --profile cpu up -d
```

#### NVIDIA GPU

> [!NOTE]
> For more guidance, please see
> [Ollama Docker instructions](https://github.com/ollama/ollama/blob/main/docs/docker.md).

```bash
docker compose --profile gpu-nvidia up -d
```

#### AMD GPU

##### AMD on Windows
Install Ollama directly on your Windows system.
For more guidance, please see [Ollama Windows](https://github.com/ollama/ollama/blob/main/docs/windows.md)
```powershell
docker compose --profile gpu-amd-win up -d
```

##### AMD on Linux
```bash
docker compose --profile gpu-amd-linux up -d
```

> [!NOTE]
> You may need to configure LLVM overrides to get ROCm to work with Ollama. For more guidance, please see
> [Ollama GPU Overrides on Linux](https://github.com/ollama/ollama/blob/main/docs/gpu.md#overrides-on-linux)

#### Apple Silicon
While Ollama supports GPU acceleration on Apple Silicon via the Metal API, Docker cannot access the GPU/Neural Engine. For the best performance, it is recommended to run Ollama directly on your Mac.

You can run Ollama on your Mac with one of the options below:
 - [Download Ollama](https://ollama.com/download/mac)
 - Install via homebrew - `brew install ollama`

If you choose to run Ollama natively and only want to run OpenWebUI in Docker:
```bash
docker compose --profile macos up -d
```

### 3. Accessing Services

*   **OpenWebUI**: Open your web browser and go to `http://localhost:8080`.
*   **Ollama API**: `http://localhost:11434` (if Ollama is running in Docker or on the same host).

### 4. Downloading Models

You can download models in a few different ways:

#### Using Ollama CLI
If you have Ollama installed natively or want to execute commands inside the Docker container:
```bash
ollama pull <model_name>
```

#### Using Ollama Docker Command
To pull a model using the Ollama instance running in Docker:
```bash
docker exec -it ollama ollama pull <model_name>
```

#### Using OpenWebUI Interface
Navigate to the OpenWebUI interface (`http://localhost:8080`), go to Settings > Models, and use the 'Pull a model' field to download models from Ollama's library.

#### Using Hugging Face
Ollama can also pull models directly from Hugging Face. For more details, see: [Hugging Face & Ollama Integration](https://huggingface.co/docs/hub/en/ollama).

### 5. Stopping Services

To stop the running containers:

```bash
docker compose --profile "*" down
```

## Directory Contents
*   `README.md`: This file.
*   `docker-compose.yml`: Docker Compose configuration for running Ollama and OpenWebUI with different profiles.
*   `.env.example`: Example environment file for potential custom configurations (if used).

## Official Documentation & Further Resources

### Official Tool Documentation

For more in-depth information about the tools used in this setup, refer to their official documentation:

*   **Ollama:** [Ollama GitHub Documentation](https://github.com/ollama/ollama/tree/main/docs)
*   **OpenWebUI:** [OpenWebUI Documentation](https://docs.openwebui.com/)
*   **Docker Compose Profiles:** [Docker Compose Profiles Documentation](https://docs.docker.com/compose/profiles/)

### Troubleshooting

*   **Ollama Troubleshooting:** See [Ollama Troubleshooting Guide](https://github.com/ollama/ollama/blob/main/docs/troubleshooting.md)
*   **Open-WebUI Troubleshooting:** See [Open-WebUI Troubleshooting Docs](https://docs.openwebui.com/troubleshooting/)
*   **Port Conflicts:** If `8080` or `11434` are in use on your system, you may need to edit the `ports` section in the `docker-compose.yml` file for the relevant service(s) to assign different host ports.