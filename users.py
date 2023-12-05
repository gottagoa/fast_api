from fastapi import APIRouter
from pydantic import BaseModel

user_router=APIRouter(prefix='/user', tags=['users'])



@user_router.get('/{user_id}')
async def get_user(user_id:int):
    return {'message':f'Hello, {user_id}'}


class User(BaseModel):
    name:str
    age:int



@user_router.post('/')
async def create_user(user: User):
    return {'message':f'Hello, {user.name}'}


@user_router.delete('/{user_id}')
async def delete_user(user_id:int):
    return {'message':f'Hello, {user_id}'}


@user_router.post('/{user_id}')
async def update_user(user_id:int, user: User):
    return {'message':f'Hello, {user_id}'}


@user_router.get('/')
async def get_users():
    return {'message':'Hello'}