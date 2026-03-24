from fastapi import FastAPI, WebSocket
from Agent.Orchestator import graph
app = FastAPI()
@app.websocket("/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()

    while True:
        user_input = await websocket.receive_text()

        result = graph.invoke({
            "user_input": user_input
        })

        await websocket.send_text(result["response"])


