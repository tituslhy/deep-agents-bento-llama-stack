# Deep Agents with BentoML and Llama Cloud
This repository explores the use of Deep Agents with MCP tools from Llama Cloud and LLMs served by vLLM on Bento Cloud.

## BentoML
### To deploy Llama3.1-8b-Instruct on BentoML
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

### To deploy Qwen3-8b (a reasoning LLM) on BentoML:
```
bentoml cloud login
```

Followed by:
```
cd services/2. reasoning_service
```

and:
```
bentoml deploy service:LLM --instance-type "gpu.l4.1"
```

## Setup
This repository uses the uv package installer.

To create a virtual environment with the dependencies installed, simply type in your terminal:
```
uv sync
```

### Notes
- [Deep Agent](https://github.com/hwchase17/deepagents) is a LangGraph graph and can be invoked like a LangGraph react agent.