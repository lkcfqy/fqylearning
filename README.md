# 🌟 FQY Learning Agent 🧠✨

Welcome to **FQY Learning**! 🚀 This is an intelligent, graph-powered conversational AI agent designed to learn, reason, and remember! Built with a modern tech stack, it combines the generative magic of Large Language Models with the structured knowledge of Graph Databases. 🕸️📚

## ✨ Core Features 🛠️

* 💬 **Interactive Chat UI**: A beautiful, real-time web interface powered by **Chainlit**.
* 🕸️ **Knowledge Graph Integration**: Uses a Graph Database to store relationships, concepts, and data, allowing the agent to perform deep, structured reasoning.
* 🧠 **Persistent Memory**: The agent remembers past interactions and context to provide continuous, personalized responses!
* 🤖 **Smart LLM Core**: Modular architecture for language models and agent orchestration.
* 🐳 **Docker Ready**: Instantly spin up your backend environment (like your Graph DB) using Docker Compose!

## 📂 Project Structure 🗺️

Here's a quick tour of our neat and tidy codebase:

* 📄 `app.py`: The main Chainlit application entry point. 🚀
* 📄 `docker-compose.yml`: Infrastructure configuration for easy deployment. 🐳
* 📄 `requirements.txt`: Python dependencies. 📦
* 📄 `plan.md`: The blueprint and roadmap for the project! 🗺️
* 📁 `src/`: The brain of the operation! 🧩
    * `agent.py`: Agent logic, routing, and tool execution. 🕵️‍♂️
    * `config.py`: Environment variables and configuration settings. ⚙️
    * `graph_db.py`: Database connection and graph query management. 🔗
    * `memory.py`: Conversation history and context management. 📝
    * `model.py`: LLM initialization and wrapping. 🗣️

## 🚀 Getting Started 🏃‍♀️💨

Ready to chat with your new Graph-powered friend? Follow these steps!

### 1. Set Up the Environment 🌱
Clone the repository and install the required dependencies:
```bash
pip install -r requirements.txt

```

### 2. Start the Graph Database 🐳

Make sure Docker is running on your machine, then spin up the required services:

```bash
docker-compose up -d

```

### 3. Configure Your Settings ⚙️

Make sure you review `src/config.py` (or create a `.env` file) to set up your LLM API keys and Graph Database credentials!

### 4. Run the App! 🎉

Launch the Chainlit interactive UI:

```bash
chainlit run app.py -w

```

*Pop open your browser and start exploring the knowledge graph!* 🌐✨

---

*Built with ❤️ for smarter learning and graph-based AI exploration!* 🚀
