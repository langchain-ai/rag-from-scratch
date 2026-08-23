# RAG From Scratch

LLMs are trained on a large but fixed corpus of data, limiting their ability to reason about private or recent information. Fine-tuning is one way to mitigate this, but is often [not well-suited for factual recall](https://www.anyscale.com/blog/fine-tuning-is-for-form-not-facts) and [can be costly](https://www.glean.com/blog/how-to-build-an-ai-assistant-for-the-enterprise).
Retrieval augmented generation (RAG) has emerged as a popular and powerful mechanism to expand an LLM's knowledge base, using documents retrieved from an external data source to ground the LLM generation via in-context learning. 
These notebooks accompany a [video playlist](https://youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x&feature=shared) that builds up an understanding of RAG from scratch, starting with the basics of indexing, retrieval, and generation. 
![rag_detail_v2](https://github.com/langchain-ai/rag-from-scratch/assets/122662504/54a2d76c-b07e-49e7-b4ce-fc45667360a1)
 
[Video playlist](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x)


The original notebooks contained code from 2 years ago some of which was updated so these notebooks have code that actually run in aug 2026.
Also instead of OpenAI I used GROQ api with model "qwen/qwen3.6-27b" and "openai/gpt-oss-120b" for embeddings I used  huggingface model "all-MiniLM-L6-v2"
Later on from part 12 and onwards when these models could not handle the large context I switched to openrouter that used the OpenAI library but with "openrouter/free" that automatically decides the appropriate model for the request. 
the last notebook from part 15 onwards didn't had anycode that was actually used in the tutorial so I didn't tried that.