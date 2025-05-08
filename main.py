from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(message: Message):
    # Simulate a response from an LLM
    responses = [
        "Hello! How can I assist you today?",
        "I'm here to help you with your queries.",
        "What would you like to know?",
        "Feel free to ask me anything!"
    ]
    return {"response": random.choice(responses)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)