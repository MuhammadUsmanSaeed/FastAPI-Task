from typing import List, Optional

from pydantic import BaseModel, EmailStr


class ItemSchemaCls:
    def __init__(self, *, name_of_item: str, email: str, password: str):
        self.name_of_item = name_of_item
        self.email = email
        self.password = password


class Item_Schema(BaseModel):
    name_of_item: str
    location_of_lost_or_found_item: str
    description_of_item: str

    class Config:
        orm_mode = True


class UserSchemaCls:
    def __init__(self, *, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password


class User_Schema(BaseModel):
    name: str
    email: str
    password: str


class MyUserSchemaCls:
    def __init__(self, *, name: str, email: str):
        self.name = name
        self.email = email


class My_User_Schema(BaseModel):
    name: str
    email: str
    items: List[Item_Schema] = []

    class Config:
        orm_mode = True


class MyItemSchemaCls:
    def __init__(self, *, name_of_item: str, location_of_lost_or_found_item: str, description_of_item: str):
        self.name_of_item = name_of_item
        self.location_of_lost_or_found_item = location_of_lost_or_found_item
        self.description_of_item = description_of_item


class My_Item_Schema(Item_Schema):
    name_of_item: str
    location_of_lost_or_found_item: str
    description_of_item: str
    owner: My_User_Schema

    class Config:
        orm_mode = True


class LoginCls:
    def __init__(self, *, username: str, password: str):
        self.username = username
        self.password = password


class Login(BaseModel):
    username: str
    password: str


class TokenCls:
    def __init__(self, *, access_token: str, token_type: str):
        self.access_token = access_token
        self.token_type = token_type


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenDataCls:
    def __init__(self, *, email: str):
        self.email = email


class TokenData(BaseModel):
    email: Optional[str] = None


class EmailCls:
    def __init__(self, *, email: EmailStr):
        self.email = email


class EmailSchema(BaseModel):
    email: List[EmailStr]
