# Local AI Setup with Ollama and OpenWebUI using Docker Compose

This guide explains how to set up **Ollama** (a tool for running large language models) and **OpenWebUI** (a web interface for AI models).

## Table of Contents

- [Hardware Requirements](#hardware-requirements)
  - [GPU Requirements](#gpu-requirements)
- [Software Requirements](#software-requirements)

## Usage

See [USAGE.md](./USAGE.md) for details on getting started

## Hardware Requirements

For decent results, the minimum requirements are:
- **CPU:** >4 cores
- **RAM:** >8GB
- **Storage:** >50GB

For optimal performance, it's highly recommended to use a GPU with this setup. CPU inference is **painfully** slow.

### GPU Requirements
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

## Software Requirements

- [Docker](https://docs.docker.com/get-started/get-docker/)

*For NVIDIA GPUs*
- [NVIDIA Drivers](https://www.nvidia.com/Download/index.aspx)
- [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)

*For AMD GPUs*
- [ROCm Drivers](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/)

>[!NOTE]
>ROCm on Windows is 
## Official Documentation

For more in-depth information about the tools used in this setup, refer to their official documentation:

*   **Ollama:** [https://github.com/ollama/ollama/tree/main/docs](https://github.com/ollama/ollama/tree/main/docs)
*   **OpenWebUI:** [https://docs.openwebui.com/](https://docs.openwebui.com/)
*   **Docker Compose Profiles:** [https://docs.docker.com/compose/profiles/](https://docs.docker.com/compose/profiles/)