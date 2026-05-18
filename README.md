# fqylearning

一个本地化 GraphRAG/长期记忆聊天原型。项目把 Chainlit、LangGraph、Neo4j、Ollama 兼容模型和知识图谱抽取流程组合起来，尝试把对话内容沉淀为实体与关系，再在后续对话中作为上下文使用。

## 当前状态

当前代码已经实现了 Chainlit 聊天入口、LangGraph 工作流、LLM 抽取实体/关系并写入 Neo4j 的路径，以及 Neo4j fulltext index 初始化。

检索侧仍是占位实现：`retrieve_memory()` 里保留了 Cypher 查询草稿，但当前实际返回的是 `"Context from graph..."`。向量检索、reranker、LangFuse 观测集成等还没有真正接入主流程。

## 主要模块

- `app.py`：Chainlit 聊天入口。
- `src/agent.py`：LangGraph 工作流，包含 retrieve、generate、update_memory 三步。
- `src/memory.py`：知识抽取、Neo4j 写入和索引初始化。
- `src/model.py`：本地 LLM 和 embedding 模型封装。
- `src/graph_db.py`：Neo4j 连接。
- `src/config.py`：Neo4j、Ollama、模型名等配置。
- `docker-compose.yml`：Neo4j 与 LangFuse 相关服务。

## 快速开始

启动服务：

```bash
docker compose up -d
```

准备 Python 环境：

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

准备本地模型，例如：

```bash
ollama pull deepseek-r1:8b
```

启动 Chainlit：

```bash
chainlit run app.py
```

## 配置说明

默认配置在 `src/config.py` 中：

- Neo4j：`bolt://localhost:7687`
- 默认用户名：`neo4j`
- 默认密码：`password`
- LLM：`deepseek-r1:8b`
- Embedding：`BAAI/bge-m3`

生产或公开部署前请修改默认密码，并用环境变量或安全配置管理密钥。

## 待完善事项

- 将 `retrieve_memory()` 从占位返回改为真实 Neo4j fulltext/vector 检索。
- 接入 embedding 写入与相似度召回。
- 明确 LangFuse 的实际使用路径。
- 补充端到端测试和最小样例数据。

## 许可证

当前仓库未包含独立 `LICENSE` 文件。如需公开复用或分发，请先补充明确的开源许可证。
