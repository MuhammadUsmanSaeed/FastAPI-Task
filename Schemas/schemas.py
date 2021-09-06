from pydantic import BaseModel


class Item_Schema(BaseModel):
    name_of_item: str
    location_of_lost_or_found_item: str
    description_of_item: str


class User_Schema(BaseModel):
    name:str
    email:str
    password:str


class My_User_Schema(BaseModel):
    name:str
    email:str

    class Config():
        orm_mode = True


class My_Item_Schema(Item_Schema):
    name_of_item: str
    location_of_lost_or_found_item: str
    description_of_item: str
    creator: My_User_Schema

    class Config():
        orm_mode = True
