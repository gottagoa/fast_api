from fastapi import FastAPI, Response
from pydantic import BaseModel
from starlette.responses import Response, JSONResponse, StreamingResponse
from typing import Optional
from io import BytesIO

app=FastAPI()

class ResponseExample(BaseModel):
    message: str
    message3: Optional[str]=None


def generator():
    yield b'some binary date'
    yield b'another binary data'
    yield b'more binary data'
    

@app.get('/', response_model=ResponseExample)
async def root(response: Response):
    # response=JSONResponse(content={'message':'Hello World', 'message3': 'Hello world3'}, headers={'X-Cat':'meow'})
    response.set_cookie(key='fakesession', value='fake-cookie-session-value')
    response.headers['X-Cat-Dog']='alone in the world'
    return {'message':'Hello World', 'message3': 'Hello world3'}


# @app.get('/', response_model=ResponseExample)
# async def root():
#     return StreamingResponse(generator())


@app.get('/hello/{name}')
async def say_hello(name: str):
    return {'message': f"Hello {name}"}


ResponseExample(**{'message':'Hello World', 'message2':'Hello world2'})