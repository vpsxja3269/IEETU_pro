from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    password: str

class Post(BaseModel):
    title: str
    content: str
    author: str

users = []
posts = []

@app.post("/users/", response_model=User)
def create_user(user: User):
    users.append(user)
    return user

@app.get("/users/", response_model=List[User])
def get_users():
    return users

@app.post("/posts/", response_model=Post)
def create_post(post: Post):
    posts.append(post)
    return post

@app.get("/posts/", response_model=List[Post])
def get_posts():
    return posts

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
