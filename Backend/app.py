from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    password: str

class Post(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    author: str

users = []
posts = []
post_id_counter = 1

@app.post("/users/", response_model=User)
def create_user(user: User):
    users.append(user)
    return user

@app.get("/users/", response_model=List[User])
def get_users():
    return users

@app.post("/posts/", response_model=Post)
def create_post(post: Post):
    global post_id_counter
    post.id = post_id_counter
    post_id_counter += 1
    posts.append(post)
    return post

@app.get("/posts/", response_model=List[Post])
def get_posts():
    return posts

@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    global posts
    posts = [post for post in posts if post.id != post_id]
    return {"message": "Post deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
