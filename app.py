from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/chat")
async def chat():
    return FileResponse("chat.html")

@app.get("/page")
async def page():
    return FileResponse("page.html")