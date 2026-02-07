# 实时学习无限记忆智能体 (Real-time Learning Infinite Memory Agent)

这是一个基于本地大模型 (**DeepSeek-R1-Distill-Llama-8B**) 和图数据库 (**Neo4j**) 构建的智能体。它具备**无限记忆**能力，能够从对话中实时提取知识并构建知识图谱。

## ✨ 核心功能
*   **🧠 深度推理**: 使用 DeepSeek-R1 系列模型进行思维链 (CoT) 推理。
*   **♾️ 无限记忆**: 
    *   **GraphRAG**: 自动从对话中提取实体和关系，存入 Neo4j 图数据库。
    *   **上下文感知**: 聊天时自动检索相关历史记忆。
*   **⚡ 极速响应**: 
    *   **流式输出 (Streaming)**: 像打字机一样即时显示回复。
    *   **异步记忆**: 记忆存储在后台运行，不阻塞对话。
*   **🔍 混合检索**: 结合语义搜索 (BGE-M3) 和图谱查询。

## 🛠️ 技术栈
*   **LLM**: DeepSeek-R1-Distill-Llama-8B (via Ollama)
*   **Embedding**: BAAI/bge-m3 (HuggingFace)
*   **Database**: Neo4j (with APOC)
*   **Framework**: LangChain, LangGraph
*   **UI**: Chainlit

## 🚀 快速开始

### 1. 前置要求
确保您已安装：
*   [Docker](https://www.docker.com/) & Docker Compose
*   [Ollama](https://ollama.com/)
*   [Conda](https://docs.conda.io/en/latest/) (推荐)

### 2. 启动基础设施
```bash
# 1. 启动 Neo4j 数据库和 LangFuse (可选)
docker compose up -d

# 2. 启动 Ollama 并拉取模型 (如果未拉取)
ollama serve
ollama pull deepseek-r1:8b
```

### 3. 安装依赖
```bash
# 创建并激活环境
conda create -n fqylearning python=3.10
conda activate fqylearning

# 安装 Python 包
pip install -r requirements.txt
```

### 4. 运行应用
```bash
chainlit run app.py -w
```
应用将在浏览器自动打开，地址通常为 `http://localhost:8000`。

## ⚙️ 配置说明
主要配置文件位于 `src/config.py`，您可以修改环境变量来调整设置：
*   `LLM_MODEL`: 使用的模型名称 (默认 `deepseek-r1:8b`)
*   `NEO4J_URI`: 图数据库地址
*   `OLLAMA_BASE_URL`: Ollama 服务地址

## 📂 目录结构
*   `src/`: 核心源代码 (智能体逻辑、记忆模块、数据库连接)
*   `app.py`: Chainlit 用户界面应用入口
*   `neo4j/`: Neo4j 数据持久化目录
*   `requirements.txt`: Python 依赖列表

---
*Created by Antigravity*
