import fastapi
from deta import Base
from typing import Dict, Any
from fastapi.middleware.cors import CORSMiddleware

app = fastapi.FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])

config = Base("config")
questions = Base("questions")

# Config


@app.get("/config")
async def get_config():
    sub = config.get("submissions_state")
    user = config.get("user_state")
    name = config.get("display_name")
    image = config.get("display_image")
    return {
        "submissions_state": sub,
        "user_state": user,
        "display_name": name,
        "display_image": image,
    }


@app.patch("/config")
async def patch_config(value: Dict[Any, Any], key: str):
    msg = config.update(value, key)
    return msg


@app.post("/config")
async def post_config(request: fastapi.Request):
    data = await request.json()
    msg = config.put(data)
    return msg


# Questions


@app.get("/questions")
async def get_questions():
    res = questions.fetch()
    items = res.items
    while res.last:
        res = questions.fetch(last=res.last)
        items += res.items
    return items


@app.post("/questions")
async def post_questions(question: str):
    msg = questions.put({"question": question, "hidden": False, "replied": False})
    return msg


@app.patch("/questions")
async def patch_questions(value: Dict[Any, Any], key: str):
    msg = questions.update(value, key)
    return msg


@app.delete("/questions")
async def delete_questions(key: str):
    msg = questions.delete(key)
    return msg


# Answers


@app.post("/answer")
async def post_answer(key: str, answer: str):
    msg = questions.update({"reply": answer})
    return msg


# Public


@app.get("/public")
async def get_public():
    sub = config.get("submissions_state")
    user = config.get("user_state")
    name = config.get("display_name")
    image = config.get("display_image")
    return {
        "submissions_state": sub,
        "user_state": user,
        "display_name": name,
        "display_image": image,
    }
