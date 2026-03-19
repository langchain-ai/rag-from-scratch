# Minimal modernization checklist for 2026 practice

This repository is still useful for learning RAG concepts, but the original notebooks were written during the early LangChain package-split transition. Use the checklist below to keep the repo stable enough for repeated practice in 2026.

## What "minimal modernization" means here

This repo remains notebook-first on purpose. The goal is not to turn it into a full application, but to add just enough structure that you can:

1. create one reproducible environment,
2. understand which notebooks need which providers,
3. avoid stale defaults for package imports and model choices,
4. gradually refactor exercises into reusable modules later.

## Step 1: standardize the environment

- [x] Add a root `pyproject.toml` with one base dependency set.
- [x] Split optional integrations into extras:
  - `youtube`
  - `rerank`
  - `cohere`
  - `colbert`
- [ ] Generate and commit a lock file with your preferred tool (`uv lock`, `pip-tools`, or Poetry).
- [ ] Document the exact Python version you use for exercises.

## Step 2: stop relying on notebook-local installs

- [ ] Remove duplicated `! pip install ...` cells from the notebooks after your environment is working.
- [ ] Replace them with a short markdown note that points back to the root setup instructions in `README.md`.
- [ ] Keep notebook dependencies centralized in one place.

## Step 3: finish the LangChain import cleanup

The repo currently mixes pre-split and post-split import styles. When you touch a notebook, normalize imports as you go.

Search for these patterns and migrate them:

- `from langchain.text_splitter import RecursiveCharacterTextSplitter`
  - replace with `from langchain_text_splitters import RecursiveCharacterTextSplitter`
- `from langchain.prompts import ChatPromptTemplate`
  - replace with `from langchain_core.prompts import ChatPromptTemplate`
- `from langchain_community.vectorstores import Chroma`
  - prefer `from langchain_chroma import Chroma`

## Step 4: refresh model defaults

Prefer making model names easy to swap from a single notebook cell.

Recommended notebook pattern:

```python
CHAT_MODEL = "gpt-4o-mini"
EMBEDDING_MODEL = "text-embedding-3-small"
```

Then wire them into constructors explicitly:

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

llm = ChatOpenAI(model=CHAT_MODEL, temperature=0)
embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
```

## Step 5: practice in layers

Use the notebooks in this order:

1. `rag_from_scratch_1_to_4.ipynb`
2. `rag_from_scratch_5_to_9.ipynb`
3. `rag_from_scratch_10_and_11.ipynb`
4. `rag_from_scratch_12_to_14.ipynb`
5. `rag_from_scratch_15_to_18.ipynb`
6. `rag_from_scratch_retrieval_engineering.ipynb`

That sequence lets you stabilize core dense RAG first, then branch into query transformation, reranking, and retrieval evaluation.

## Step 6: next upgrades after the minimal pass

Once the repo is comfortable again, the next worthwhile upgrades are:

- extract shared helpers into `src/` modules,
- add a small local evaluation dataset,
- add a notebook smoke-test script,
- cache downloaded web content for reproducibility,
- store experiment settings in `.env.example` instead of ad hoc cells.
