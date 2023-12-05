from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List


# app=FastAPI()


# @app.get('/')
# def hello():
#     return 'Hello, world!'


app=FastAPI(
    title='Trading App'
)

fake_users =[
    {'id':1, 'role':'admin', 'name':'Bob'},
    {'id':2, 'role':'investor', 'name':'John'},
    {'id':3, 'role':'trader', 'name':'Matt'},
]


@app.get('/users/{user_id}')
def get_user(user_id:int):
    return [user for user in fake_users if user.get('id')==user_id]


fake_trades = [
    {'id':1, 'usser_id':1, 'currency':'BTC', 'side':'buy', 'price':123, 'amount':2.12},
    {'id':2, 'usser_id':1, 'currency':'BTC', 'side':'sell', 'price':125, 'amount':2.12},
]

# @app.get('/trades')
# def get_trades(limit: int, offset: int):
#     return fake_trades[offset:][:limit]

'''
limit-номер пагинаций. то есть если 10 пунктом из первой пагинации
offset-id запроса. id указывается индексом, то есть если мы хотим 1 сделку с id 1 то указываем 2
'''
@app.get('/trades')
def get_trades(limit: 1, offset: 0):
    return fake_trades[offset:][:limit]



fake_users2=[
    {'id':1, 'role':'admin', 'name':'Bob'},
    {'id':2, 'role':'investor', 'name':'John'},
    {'id':3, 'role':'trader', 'name':'Matt'},
]

@app.post('/users/{user_id}')
def change_user_name(user_id: int, new_name: str):
    current_user=list(filter(lambda user: user.get('id')==user_id, fake_users2))[0]
    current_user['name']=new_name
    return {'status':200, 'data':current_user}


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str
    side: str
    price: float= Field(ge=0)
    amount: float

@app.post('/trades')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {'status':200, 'data':fake_trades}

