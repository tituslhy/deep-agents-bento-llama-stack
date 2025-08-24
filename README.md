# Deep Agents with BentoML and Llama Cloud
This repository explores the use of Deep Agents with MCP tools from Llama Cloud and LLMs served by vLLM on Bento Cloud.

This repository is a resource to the Medium Article series "Creating a Hypermodern Generative AI Application"

The articles and their respective notes are enumerated as below.

## Act One: Deploying a vLLM service on Bento Cloud
Medium Article: [🥡 Would You Like an LLM with That? — A Bento Cloud Drive-Thru](https://medium.com/mitb-for-all/would-you-like-an-llm-with-that-a-bento-cloud-drive-thru-7e70f77277d2)
<p align="center">
    <img src="./images/ActOne/ActOne.png" height="400">
</p>

#### To deploy Llama3.1-8b-Instruct on BentoML
```
bentoml cloud login
```

Followed by:
```
cd services/1. standard_service
```

Register your HuggingFace Token:
```
bentoml secret create huggingface HF_TOKEN=$HF_TOKEN
```

and:
```
bentoml deploy service:LLM --instance-type "gpu.l4.1" --secret huggingface
```

#### To deploy Qwen3-8b (a reasoning LLM) on BentoML:
```
bentoml cloud login
```

Followed by:
```
cd services/2. reasoning_service
```

and:
```
bentoml deploy service:LLM --instance-type "gpu.l4.1" --scaling-min 1 --scaling-max 3
```

## Act Two: The Hypermodern RAG application
Coming soon!

## Setup
This repository uses the uv package installer.

To create a virtual environment with the dependencies installed, simply type in your terminal:
```
uv sync
```

### Notes
- [Deep Agent](https://github.com/hwchase17/deepagents) is a LangGraph graph and can be invoked like a LangGraph react agent.