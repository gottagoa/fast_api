from fastapi import FastAPI, Response, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from starlette.responses import Response, FileResponse, JSONResponse,StreamingResponse
from starlette.websockets import WebSocket
from starlette.background import BackgroundTasks
import logging
import uvicorn
from datetime import datetime
import httpx
from httpx import Request
import asyncio


logger=logging.Logger(__name__)

app=FastAPI()

def paginate(limit: Optional[int]=10, offset: Optional[int] =0)-> dict:
    return {
        'limit':limit,
        'offset':offset,
    }

def auth_user(token: str):
    pass

async def very_slow_function():
    await asyncio.sleep(10)


@app.get('/users')
async def get_users(pagination: dict=Depends(paginate)):
    now=datetime.now()
    users=[
        {
            'name':'Nicolay',
            'is_online':True,
        },
        {
            'name':'Vasya',
            'is_online':False,
        }
    ]
    response_time=datetime.now()-now
    return users[pagination['offset']: pagination['offset']+pagination['limit']]



@app.get('/chats')
async def get_chats():
    chats=[
        {
            'name':'chat 1',
            'members':2,
        },
        {
            'name':'chat ',
            'members':1,
        }
    ]
    return chats


@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    now=datetime.now()
    response= await call_next(request)
    response.headers['X-Process-Time']=str(datetime.now()-now())
    return response


@app.on_event('startup')
async def startup_event():
    print('startup')

@app.on_event('shutdown')
async def shutdown_event():
    print('shutdown')


@app.get('/slow-function')
async def slow_functiom(background_tasks: BackgroundTasks):
    await very_slow_function()
    return {'message':'Hello world!'}


if __name__ == '__main__':
    uvicorn.run(app, hosts='0.0.0.0', port=8000)