from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import random
import lite_llm  # Assuming lite_llm is the library for LLM integration

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(message: Message):
    # Use LiteLLM to get a response
    llm_response = lite_llm.get_response(message.message)  # Placeholder for actual LLM call
    return {"response": llm_response}

@app.post("/upload-text")
async def upload_text(file: UploadFile = File(...)):
    content = await file.read()
    # Process the text file content
    return {"filename": file.filename, "content": content.decode()}

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    content = await file.read()
    # Process the image file content
    return {"filename": file.filename, "size": len(content)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)