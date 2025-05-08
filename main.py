from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import random
import lite_llm  # Assuming lite_llm is the library for LLM integration

app = FastAPI()
conversation_history = []

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(message: Message):
    global conversation_history
    conversation_history.append(message.message)
    
    # Use LiteLLM to get a response
    llm_response = lite_llm.get_response(" ".join(conversation_history))  # Send the entire conversation as context
    conversation_history.append(llm_response)  # Store the LLM response
    return {"response": llm_response}

@app.post("/upload-text")
async def upload_text(file: UploadFile = File(...)):
    content = await file.read()
    return {"filename": file.filename, "content": content.decode()}

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    content = await file.read()
    return {"filename": file.filename, "size": len(content)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)