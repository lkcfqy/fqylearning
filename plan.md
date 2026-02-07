# 实时学习无限记忆智能体 - 项目计划

## 1. 项目概述
本项目旨在构建一个具备实时学习能力和无限记忆的智能体。利用 GraphRAG 技术结合 Neo4j 图数据库实现长期记忆，使用 DeepSeek-R1-Distill-Qwen-14B 作为核心推理引擎，并通过 LangGraph 管理智能体工作流。

**硬件环境**:
- CPU: i9-9900KF
- RAM: 32GB
- GPU: RTX 3080 10GB
- OS: Ubuntu 24.04

**核心技术栈**:
- **LLM**: DeepSeek-R1-Distill-Qwen-14B (需量化以适应 10GB 显存)
- **图数据库**: Neo4j
- **RAG**: GraphRAG, BGE-M3 (Embedding), BGE-Reranker (Reranking)
- **编排工具**: LangChain, LangGraph
- **可观测性**: LangFuse

---

## 2. 详细实施步骤

### 第一阶段：环境搭建与模型部署
*目标：在本地环境成功运行大模型、数据库及监控工具。*

1.  **系统基础环境**:
    - [x] 安装 Nvidia Drivers & CUDA Toolkit 12.x
    - [x] 安装 Docker & Docker Compose
    - [x] 配置 Python 3.10+ 虚拟环境 (Conda env: fqylearning)

2.  **数据库与工具链 (Docker)**:
    - [x] **Neo4j**: 部署 Neo4j Community Edition (启用 APOC 插件)
    - [x] **LangFuse**: 本地部署 LangFuse (Docker Compose) 用于链路追踪

3.  **模型服务化**:
    - [x] **LLM 推理**:
        - 使用 Ollama 或 vLLM 部署 `DeepSeek-R1-Distill-Qwen-14B`。
        - **注意**: 由于 10GB 显存限制，必须使用 **4-bit 量化 (Q4_K_M)** 版本。如果是 vLLM，需开启 `--quantization awq` 或类似选项，或部分把层卸载到 CPU。
    - [x] **Embedding/Rerank**:
        - 本地部署 `BAAI/bge-m3` 和 `BAAI/bge-reranker-v2-m3`。
        - 建议使用 GPU 推理 Embedding，显存不足时切换至 CPU。

### 第二阶段：核心模块开发
*目标：构建基于图数据库的记忆模块和检索增强生成链路。*

4.  **知识图谱构建 (GraphRAG Pipeline)**:
    - [x] 设计图谱 Schema (实体、关系、属性)。
    - [x] 实现非结构化文本到图谱的转换 (Text to Graph)：使用 LLM 提取实体和关系。
    - [x] 集成 Neo4jVector (混合索引：向量 + 关键词)。

5.  **记忆模块 (Infinite Memory)**:
    - [x] **短期记忆**: 基于 LangGraph 的 Checkpoint 机制 (对话历史)。
    - [x] **长期记忆**: 将对话摘要和关键信息写入 Neo4j 图谱。
    - [x] **记忆检索**: 实现基于图查询 (Cypher) 和向量相似度的混合检索策略。

### 第三阶段：智能体构建与编排
*目标：使用 LangGraph 串联感知、记忆、推理和行动。*

6.  **LangGraph 工作流设计**:
    - [x] 定义状态 (State: 包含消息、上下文、图实体等)。
    - [x] **节点开发**:
        - `Retrieve`: 混合检索 (BGE-M3 + Neo4j)。
        - `Rerank`: 使用 BGE-Reranker 对检索结果排序。
        - `Reason`: 使用 DeepSeek-R1 进行思维链 (CoT) 推理。
        - `UpdateMemory`: 异步更新图数据库知识。
    - [x] 构建条件边 (Conditional Edges)。

7.  **LangFuse 埋点**:
    - [ ] 全链路接入 LangFuse Tracing，监控 Token 消耗、延迟和回复质量。

### 第四阶段：交互与优化
*目标：提供友好的交互界面并持续优化性能。*

8.  **用户界面**:
    - [x] 使用 Streamlit 或 Chainlit 开发聊天界面。
    - [x] 展示实时推理过程 (Thought Process) 和检索到的图谱上下文。

9.  **性能调优**:
    - [x] 优化 Prompt Engineering 以适配 Qwen-14B 的能力。
    - [x] 调整 Neo4j 索引策略以加快检索速度。
    - [x] 显存管理优化 (确保 LLM 和 Embedding 模型共存不 OOM)。

---

## 3. 硬件资源分配策略
- **DeepSeek-R1-14B (Q4)**: 约占用 8-9 GB VRAM。
- **BGE-M3 / Reranker**: 建议使用 CPU 推理或在需要时动态加载/卸载，或者利用剩余的 ~1GB VRAM (非常紧张) -> **推荐**: 放到 CPU 或使用量化版 Embedding。
- **Neo4j**: 使用系统内存 (分配 4-8 GB JVM Heap)。
- **System**: 预留 4GB+ 给 Ubuntu 系统。
