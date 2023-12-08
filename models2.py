from pydantic import BaseModel, Field, validator, HttpUrl, EmailStr
from typing import Optional, Literal
import random
import datetime

def generate_random_name()-> str:
    names=['Nicolay','Ivan']
    return random.choice(names)

class Phone(BaseModel):
    phone:str

class Address(BaseModel):
    country:str
    city:str
    # phone:Phone

class User(BaseModel):
    name:str=Field(default_factory=generate_random_name)
    age:int=Field(gt=0,lt=130, default=20)
    password:str
    password2:str
    non_required_param: Optional[str]=None
    addresses: Optional[list[Address]]
    locale: Literal['ru-RU', 'en=US']
    created_date: datetime.datetime=Field(default_factory=datetime.datetime.now)
    avatar_url: HttpUrl
    email: Optional[EmailStr]


    @validator('password')
    def validate_password(cls, password, values, **kwargs):
        if '!' in password:
            raise ValueError('not in password')
        return password

    @validator('password2')
    def validate_password2(cls, password2, values, **kwargs):
        if password2!=values['password']:
            raise ValueError("passwords dont't match")
        return password2

address=Address(city='Moscow', country='Russia')
user=User(
    name='Nicolay', 
    age=26,
    password='12345', 
    password2='12345',
    addresses=[address], 
    locale='ru-RU',
    avatar_url='http://avatar.com',
    email='dj.@gmail.com'
)

print(user.json())