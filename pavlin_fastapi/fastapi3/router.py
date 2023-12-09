from fastapi import FastAPI
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from ...users import User
from ...users import user_router

app=FastAPI()

v1_router=APIRouter(prefix='/v1', tags=['v1'])
v2_router=APIRouter(prefix='/v2', tags=['v2'])

v1_router.include_router(user_router)
v2_router.include_router(user_router)

app.include_router(v1_router)
app.include_router(v2_router)

class User(BaseModel):
    name:str
    age:int

@app.get('/')
async def root(name:str, age:int):
    return {'message':f'Hello {name}, yoa sre {age} years old'}


@app.post('/post')
async def post(users: Optional[list[User]]=None):
    if users is None:
        users=[]
    names=[user.name for user in users]
    return {'message':f'Hello, {",".join(names)}'}


@app.get('/{names}')
async def get_user(name:str):
    return {'message':f'Hello, {name}'}


@app.get('/users/{user_id}')
async def get_user(user_id:int):
    return {'message':f'Hello, {user_id}'}

@app.post('/users')
async def create_user(user: User):
    return {'message':f'Hello, {user.name}'}

@app.delete('/users/{user_id}')
async def delete_user(user_id:int):
    return {'message':f'Hello, {user_id}'}

@app.post('/users/{user_id}')
async def update_user(user_id:int, user: User):
    return {'message':f'Hello, {user_id}'}


@app.get('/users/')
async def get_users():
    return {'message':'Hello'}