import os
from dotenv import load_dotenv, find_dotenv

from fastmcp import FastMCP
from llama_index.indices.managed.llama_cloud import LlamaCloudIndex
from llama_index.llms.ollama import Ollama

from typing import Annotated
from openinference.instrumentation.llama_index import LlamaIndexInstrumentor
from phoenix.otel import register

_ = load_dotenv(find_dotenv())

os.environ["PHOENIX_COLLECTION_ENDPOINT"] = "http://localhost:6006"
tracer_provider = register()
LlamaIndexInstrumentor().instrument(tracer_provider=tracer_provider)

LLAMA_CLOUD_API_KEY = os.environ['LLAMA_CLOUD_API_KEY']
kwargs = {
    'dense_similarity_top_k': 10,
    'sparse_similarity_top_k': 20,
    'enable_reranking': True,
    'alpha': 0.5,
    'rerank_top_n': 8
}
llm = Ollama(model="qwen3:latest", request_timeout=6000, temperature=0)
mcp = FastMCP(
    name='Alita and MCP Zero Knowledge Base',
    port=8000,
    host="0.0.0.0",
)

@mcp.tool()
async def alita_documentation(
    query: Annotated[str, "The question to ask about the Alita framework in complete sentences."]
) -> str:
    """Use this tool to answer questions about the Alita framework"""
    alita_index = LlamaCloudIndex(
        name="alita-index",
        project_name="Default",
        organization_id="bf9b425c-54cb-4182-a93f-8ac6aed04348",
        api_key=LLAMA_CLOUD_API_KEY,
    )
    alita_engine = alita_index.as_query_engine(llm=llm, **kwargs)
    response = alita_engine.query(query + " Be verbose and exhaustive in your reply.")
    return str(response)

@mcp.tool()
async def mcp_zero_documentation(
    query: Annotated[str, "The question to ask about the MCP zero framework in complete sentences."]
) -> str:
    """Use this tool to answer questions about the MCP Zero framework"""
    mcp_zero_index = LlamaCloudIndex(
        name="mcp-zero-index",
        project_name="Default",
        organization_id="bf9b425c-54cb-4182-a93f-8ac6aed04348",
        api_key=LLAMA_CLOUD_API_KEY,
    )
    mcp_zero_engine = mcp_zero_index.as_query_engine(llm=llm, **kwargs)
    response = mcp_zero_engine.query(query + " Be verbose and exhaustive in your reply.")
    return str(response)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")