import chainlit as cl
from src.agent import app_agent
from src.memory import init_indexes
from langchain_core.messages import HumanMessage, AIMessage

@cl.on_chat_start
def start():
    # Initialize Neo4j indexes
    init_indexes()
    cl.user_session.set("history", [])

@cl.on_message
async def on_message(message: cl.Message):
    """Handle incoming messages."""
    history = cl.user_session.get("history")
    history.append(HumanMessage(content=message.content))
    
    inputs = {
        "messages": history,
        "context": "" 
    }
    
    # Run the graph
    app = app_agent
    
    msg = cl.Message(content="")
    await msg.send()
    
    final_response = ""
    
    # Stream events from the graph
    async for event in app.astream_events(inputs, version="v1"):
        kind = event["event"]
        if kind == "on_chat_model_stream":
            content = event["data"]["chunk"].content
            if content:
                await msg.stream_token(content)
                final_response += content
                
    await msg.update()
    
    # Update history
    history.append(AIMessage(content=final_response))
    cl.user_session.set("history", history)
