from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import os

app = FastAPI()

@app.get("/api", response_class=PlainTextResponse)
def idea():
    key = os.environ.get("OPENAI_API_KEY")

    if key:
        return "OPENAI_API_KEY is available"
    else:
        return "OPENAI_API_KEY is NOT available"