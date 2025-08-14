# Deep Agents with BentoML and Llama Cloud
This repository explores the use of Deep Agents with MCP tools from Llama Cloud and LLMs served by vLLM on Bento Cloud.

## Setup
This repository uses the uv package installer.

To create a virtual environment with the dependencies installed, simply type in your terminal:
```
uv sync
```

To pip install dependencies from pyproject.toml file for use in Google Colab:
```
pip install .
```

### Notes
- [Deep Agent](https://github.com/hwchase17/deepagents) is a LangGraph graph and can be invoked like a LangGraph react agent.
- Deep Agent does not yet have human-in-the-loop capabilities.