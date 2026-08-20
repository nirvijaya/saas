from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from openai import OpenAI

app = FastAPI()


@app.get("/api", response_class=PlainTextResponse)
def idea():
    try:
        client = OpenAI()

        prompt = [
            {
                "role": "user",
                "content": "Come up with a new business idea for AI Agents"
            }
        ]

        response = client.chat.completions.create(
            model="gpt-5-nano",
            messages=prompt
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"OpenAI error: {type(e).__name__}: {str(e)}"