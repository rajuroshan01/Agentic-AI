from fastapi import FastAPI, WebSocket
from Agent.Orchestator import graph
app = FastAPI()
config = {"configurable": {"thread_id": "user_123"}}
@app.websocket("/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()

    while True:
        user_input = await websocket.receive_text()

        result = graph.invoke({
            "user_input": user_input
        },
        config=config
        )
        await websocket.send_text(str(result["response"]))


