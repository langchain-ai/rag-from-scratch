# RAG From Scratch

LLMs are trained on a large but fixed corpus of data, limiting their ability to reason about private or recent information. Fine-tuning is one way to mitigate this, but is often [not well-suited for factual recall](https://www.anyscale.com/blog/fine-tuning-is-for-form-not-facts) and [can be costly](https://www.glean.com/blog/how-to-build-an-ai-assistant-for-the-enterprise).
Retrieval augmented generation (RAG) has emerged as a popular and powerful mechanism to expand an LLM's knowledge base, using documents retrieved from an external data source to ground the LLM generation via in-context learning.
These notebooks accompany a [video playlist](https://youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x&feature=shared) that builds up an understanding of RAG from scratch, starting with the basics of indexing, retrieval, and generation.
![rag_detail_v2](https://github.com/langchain-ai/rag-from-scratch/assets/122662504/54a2d76c-b07e-49e7-b4ce-fc45667360a1)

[Video playlist](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x)

## Repo status

This repository is still a solid learning resource, but it is best treated as a notebook-first tutorial repo rather than a fully pinned application. The original notebooks were created during the early LangChain package-split era, so this repo now includes a minimal modernization layer to make 2026 practice less fragile.

## Quick start

### 1. Create a Python 3.11 virtual environment

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 2. Install the base notebook dependencies

```bash
pip install -e .
```

### 3. Add optional extras only when you need them

```bash
pip install -e ".[youtube]"
pip install -e ".[rerank]"
pip install -e ".[cohere]"
pip install -e ".[colbert]"
```

Or install everything used anywhere in the repo:

```bash
pip install -e ".[all]"
```

## Dependency groups

### Base

Use for the main RAG flow notebooks:

- `langchain`
- `langchain-core`
- `langchain-community`
- `langchain-openai`
- `langchain-text-splitters`
- `langchain-chroma`
- `chromadb`
- `tiktoken`
- `beautifulsoup4`
- `requests`
- `numpy`
- `jupyter`
- `ipykernel`

### Optional extras

- `youtube`: `youtube-transcript-api`, `pytube`
- `rerank`: `rank-bm25`, `sentence-transformers`, `FlagEmbedding`
- `cohere`: `cohere`, `langchain-cohere`
- `colbert`: `ragatouille`

## Notebook-to-extra mapping

| Notebook | Purpose | Extra dependencies |
| --- | --- | --- |
| `rag_from_scratch_1_to_4.ipynb` | core dense RAG | base |
| `rag_from_scratch_5_to_9.ipynb` | query transformation patterns | base |
| `rag_from_scratch_10_and_11.ipynb` | routing and query construction | base + `youtube` |
| `rag_from_scratch_12_to_14.ipynb` | RAPTOR / ColBERT-style retrieval | base + `colbert` |
| `rag_from_scratch_15_to_18.ipynb` | reranking and fusion variants | base + `cohere` |
| `rag_from_scratch_retrieval_engineering.ipynb` | hybrid retrieval evaluation | base + `rerank` |

## Recommended model defaults for practice

If you are updating the notebooks, prefer centralizing model names near the top of each notebook instead of hardcoding them in multiple cells.

```python
CHAT_MODEL = "gpt-4o-mini"
EMBEDDING_MODEL = "text-embedding-3-small"
```

Then use explicit constructors:

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

llm = ChatOpenAI(model=CHAT_MODEL, temperature=0)
embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
```

## Modernization checklist

See [`MODERNIZATION_CHECKLIST.md`](MODERNIZATION_CHECKLIST.md) for the smallest worthwhile cleanup plan that keeps this repo usable as a 2026 RAG practice workspace.

## Suggested learning order

1. `rag_from_scratch_1_to_4.ipynb`
2. `rag_from_scratch_5_to_9.ipynb`
3. `rag_from_scratch_10_and_11.ipynb`
4. `rag_from_scratch_12_to_14.ipynb`
5. `rag_from_scratch_15_to_18.ipynb`
6. `rag_from_scratch_retrieval_engineering.ipynb`
