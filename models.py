from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    name:str
    age:int
    password:str
    non_required_param: Optional[str]


# user=User(name='Nicolay', age=26, password='123456')
# print(user.json())
# user=user.dict()
user2=User.parse_obj({"name":"Nicolay", "age":26, "password":"123456", 'non_required_param':None})
print(user2)