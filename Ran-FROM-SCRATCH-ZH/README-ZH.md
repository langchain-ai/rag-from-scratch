# RAG From Scratch

LLM 通常在规模庞大但固定的数据语料上接受训练，这限制了其对私有信息或近期信息进行推理的能力。微调是缓解这一问题的一种方式，但它往往[并不适合事实性记忆](https://www.anyscale.com/blog/fine-tuning-is-for-form-not-facts)，且[成本可能较高](https://www.glean.com/blog/how-to-build-an-ai-assistant-for-the-enterprise)。

检索增强生成（RAG）已经成为扩展 LLM 知识边界的一种流行且强有力的机制。它通过从外部数据源中检索文档，并借助上下文学习将这些文档作为生成依据，从而为 LLM 的生成过程提供扎实的事实支撑。

这些 notebook 配套于一个[视频播放列表](https://youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x&feature=shared)，该系列从索引构建、检索与生成的基础概念出发，逐步建立对 RAG 的系统性理解。

### 注意
> 在运行前需要配置API和BASE URL，请不要泄露出去
> 
> 模型可以使用qwen、deepseek模型，减少403的情况发生

[English](../README.md) 

![rag_detail_v2](https://github.com/langchain-ai/rag-from-scratch/assets/122662504/54a2d76c-b07e-49e7-b4ce-fc45667360a1)
 
[视频播放列表](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x)
