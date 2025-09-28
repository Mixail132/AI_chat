"""The FastAPI routers and the chat launcher."""
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from logic.view import get_gemini_answer
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
STATIC_DIR = ROOT_DIR / "static"

app = FastAPI()
app.mount(
    "/static",
    StaticFiles(
        directory=STATIC_DIR,
        html=True
    ),
    name="static"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def serve_home():
    return FileResponse(STATIC_DIR / "chat.html")


@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = data.get("message", "")
    response = get_gemini_answer(prompt)
    return JSONResponse(
        content={"response": response}
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
