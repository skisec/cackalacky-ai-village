# Promptfoo 

This repository showcases the use of Promptfoo, an open-source command-line tool designed for evaluating and red-teaming Large Language Models (LLMs) and LLM-enabled applications. 

## Table of Contents

- [Evaluation Details](#evaluation-details)
- [Setup Instructions](#setup-instructions)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
        - [Command-Line Usage](#command-line-usage)
        - [Self-Hosted Docker Server](#self-hosted-docker-server)
- [Examples](#examples)
    - [Bias](#bias)
        - [Running the Bias example](#running-the-bias-example)
    - [Factuality](#factuality)
        - [Running the Factuality example](#running-the-factuality-example)
    - [Red Team](#red-team)
        - [Running the Red Team example](#running-the-red-team-example)
- [Official Documentation](#official-documentation)

## Setup Instructions

### Prerequisites

- [Docker](https://docs.docker.com/get-started/get-docker/)
- [Ollama](https://ollama.com/)
- [Node.js 18 or newer](https://nodejs.org/en/download/)

### Installation

#### Command-Line Usage

See the [Promptfoo Installation Guide](https://www.promptfoo.dev/docs/installation/) for guidance.

#### Self-Hosted Docker Server

See the [Promptfoo Self-Hosting Guide](https://www.promptfoo.dev/docs/usage/self-hosting/) for guidance.

## Examples

This directory contains a few sample test use cases configured to run against models hosted through Ollama, but can be adapted to run against a variety of LLM providers.

More examples can be found in Promptfoo's [official documentation](https://www.promptfoo.dev/docs/category/guides/) or [GitHub repository](https://github.com/promptfoo/promptfoo/tree/main/examples).

Each of the example test cases below are configured to use the following Ollama Models
- `gemma3:4b-it-qat`
- `phi4-mini:latest`
- `llama3.2:3b`
- `qwen3:4b`

### Bias

This test case evaluates for potential political and religious biases. The plugins used are:
- `politics`: This plugin helps identify potential vulnerabilities where the AI might inadvertently take political stances or engage in politically sensitive discussions.
    - [Plugin details](https://www.promptfoo.dev/docs/red-team/plugins/politics/)
- `religion`: This plugin tests whether the AI can express biases, make insensitive comments, or engage in inappropriate discussions related to religion.
    - [Plugin details](https://www.promptfoo.dev/docs/red-team/plugins/religion/)

#### Running the Bias example

Navigate to the `/examples/bias` directory and run:

```bash
npx promptfoo@latest redteam run
```
To view the results:
```bash
npx promptfoo@latest view
```

If running the self-hosted docker container, you can share and view the results by running:

```bash
export PROMPTFOO_REMOTE_API_BASE_URL=http://your-server-address:3000
export PROMPTFOO_REMOTE_APP_BASE_URL=http://your-server-address:3000
npx promptfoo@latest share
```

### Factuality
This test case is an adaptation of the [factuality evaluation](https://www.promptfoo.dev/docs/guides/factuality-eval/) example.

Factuality is the measure of how accurately an LLM's response aligns with established facts or reference information. Simply put, it answers the question: "Is what the AI saying actually true?"

#### Running the Factuality example

Navigate to the `/examples/factuality` directory and run

```bash
npx promptfoo@latest eval
```
To view the results:
```bash
npx promptfoo@latest view
```

If running the self-hosted docker container, you can share and view the results by running:

```bash
export PROMPTFOO_REMOTE_API_BASE_URL=http://your-server-address:3000
export PROMPTFOO_REMOTE_APP_BASE_URL=http://your-server-address:3000
npx promptfoo@latest share
```

### Red Teaming
This test case is an example of the [red teaming](https://www.promptfoo.dev/docs/red-team/). The example uses a small set of red team plugins to evaluate security and safety of the Ollama models.

#### Running the Red Teaming example

Navigate to the `/examples/redteam` directory and run

```bash
npx promptfoo@latest redteam run
```
To view the results:
```bash
npx promptfoo@latest view
```

If running the self-hosted docker container, you can share and view the results by running:

```bash
export PROMPTFOO_REMOTE_API_BASE_URL=http://your-server-address:3000
export PROMPTFOO_REMOTE_APP_BASE_URL=http://your-server-address:3000
npx promptfoo@latest share
```

## Findings

The raw CSV and JSON results of my own tests are available in the `findings` directory.

Below is a a summary of the findings:

### Bias
| Model | Score | Total Tests | Passed | Failed |
| --- | --- | --- | --- | --- |
| gemma3:4b-it-qat | 58.10% | 105 | 61 | 44 |
| phi4-mini:latest | 69.52% | 105 | 73 | 32 |
| llama3.2:3b | 81.90% | 105| 86 | 19 |
| qwen3:4b | 59.05% | 105 | 62 | 43 |

### Factuality
| Model | Score | Total Tests | Passed | Failed |
| --- | --- | --- | --- | --- |
| gemma3:4b-it-qat | 71% | 100 | 71 | 29 |
| phi4-mini:latest | 83% | 100 | 83 | 17 |
| llama3.2:3b | 83% | 100| 83 | 17 |
| qwen3:4b | 83% | 100 | 83 | 17 |

### Red Team
| Model | Score | Total Tests | Passed | Failed |
| --- | --- | --- | --- | --- |
| gemma3:4b-it-qat | - | - | - | - |
| phi4-mini:latest | - | - | - | - |
| llama3.2:3b | - | -| - | - |
| qwen3:4b | - | - | - | - |

## Observations

When I initially started testing some examples that are more 'comprehensive', it was taking an extremely long time for the tests to run with some taking more than 12 hours. 

For simplicity, these examples were set up using a relatively minimal configuration and limited number of plugins, strategies, and test cases. 

Due to this, there was a tradeoff in test accuracy which lead to false positives in the test results.

Despite this, the results do provide valuable insights into quality and security of the models used in the tests. Upon reviewing the results of the various tests, I found that there were some tests marked as 'failed' that I believe were false positives.

With a more comprehensive test setup, it is possible to reduce the number of false positives and improve the accuracy of the test results. 

Details around preventing false positives can be found [here](https://www.promptfoo.dev/docs/red-team/troubleshooting/false-positives/)

## Official Documentation

For more in-depth information about the tools used in this setup, refer to their official documentation:

*   **Promptfoo:** [https://www.promptfoo.dev/docs/](https://www.promptfoo.dev/docs/)
*   **Ollama:** [https://github.com/ollama/ollama/tree/main/docs](https://github.com/ollama/ollama/tree/main/docs)