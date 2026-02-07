from typing import TypedDict, Annotated, List, Union
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, END
from src.memory import retrieve_memory, save_to_memory
from src.model import get_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class AgentState(TypedDict):
    messages: List[BaseMessage]
    context: str

def retrieve(state: AgentState):
    """Retrieve knowledge from graph/vector store."""
    query = state["messages"][-1].content
    # Retrieve from memory (Graph + Vector)
    # In a real implementation we'd use the vector store here too
    context = retrieve_memory(query) 
    return {"context": context}

from langchain_core.runnables import RunnableConfig

async def generate(state: AgentState, config: RunnableConfig):
    """Generate answer using retrieved context."""
    messages = state["messages"]
    context = state["context"]
    query = messages[-1].content
    
    llm = get_llm()
    
    # RAG Prompt
    template = """Answer the question based only on the following context:
    {context}
    
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm | StrOutputParser()
    
    response = await chain.ainvoke({"context": context, "question": query}, config=config)
    return {"messages": [AIMessage(content=response)]}

def update_memory(state: AgentState):
    """Save conversation to memory in background."""
    messages = state["messages"]
    last_user_msg = messages[-2].content if len(messages) >= 2 else ""
    last_ai_msg = messages[-1].content
    
    # Simple strategy: Save the exchange
    text_to_save = f"User asked: {last_user_msg}. AI answered: {last_ai_msg}"
    save_to_memory(text_to_save)
    return {} # No state update needed, side effect only

# Build Workflow
workflow = StateGraph(AgentState)

workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)
workflow.add_node("update_memory", update_memory)

workflow.set_entry_point("retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", "update_memory")
workflow.add_edge("update_memory", END)

app_agent = workflow.compile()
