from fastapi import FastAPI, status, HTTPException
from fastapi.params import Depends
from fastapi_pagination import Page, LimitOffsetPage, paginate, add_pagination
from sqlalchemy.orm.session import Session

from authentication import login
from authentication import sendEmail
from authentication.hashing import Hash
from database.database import get_db
from models import models
from schemas.schemas import Item_Schema, My_Item_Schema, User_Schema, My_User_Schema
from security.oauth2 import get_current_user

app = FastAPI()

app.include_router(login.router)
app.include_router(sendEmail.router)


# Welcome Page
@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to Web-App!."}


# Get All Items
@app.get('/items/', response_model=Page[My_Item_Schema], tags=['Items'])
@app.get('/item/limit-offset', response_model=LimitOffsetPage[My_Item_Schema], tags=['Search'])
def get_item(db: Session = Depends(get_db), current_user: User_Schema =
Depends(get_current_user)):
    # my_items = db.query(models.Item).all()
    return paginate(db.query(models.Item).all())


add_pagination(app)


# Search by ID
@app.get('/items/{id}', status_code=status.HTTP_200_OK, response_model=My_Item_Schema, tags=['Items'])
def item_detail(id: int, db: Session = Depends(get_db), current_user: User_Schema =
Depends(get_current_user)):
    my_item = db.query(models.Item).get(id)

    if my_item:
        return my_item

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The item does not exists")


# Post Item
@app.post('/items/', status_code=status.HTTP_201_CREATED, tags=['Items'])
def add_item(item: Item_Schema, db: Session = Depends(get_db), current_user: User_Schema =
Depends(get_current_user)):
    new_item = models.Item(name_of_item=item.name_of_item,
                           location_of_lost_or_found_item=item.location_of_lost_or_found_item,
                           description_of_item=item.description_of_item, owner_id=1)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


# Update Item
@app.put('/items/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Items'])
def update_item(id, item: Item_Schema, db: Session = Depends(get_db), current_user: User_Schema =
Depends(get_current_user)):
    db.query(models.Item).filter(models.Item.id == id).update(
        {'name_of_item': item.name_of_item, 'location_of_lost_or_found_item': item.location_of_lost_or_found_item,
         'description_of_item': item.description_of_item})
    db.commit()
    return {'message': 'The item has been updated'}


# Delete Item
@app.delete('/items/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Items'])
def delete_item(id: int, db: Session = Depends(get_db), current_user: User_Schema =
Depends(get_current_user)):
    db.query(models.Item).filter(models.Item.id == id).delete(synchronize_session=False)
    db.commit()
    return {'message': 'Item has been deleted'}


# Create User
@app.post('/user/', status_code=status.HTTP_201_CREATED, tags=['Sign up'])
def create_user(user: User_Schema, db: Session = Depends(get_db)):
    new_user = models.User(name=user.name,
                           email=user.email,
                           password=Hash.bcrypt(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Get User
@app.get('/user/{id}', status_code=status.HTTP_200_OK, response_model=My_User_Schema, tags=['Sign up'])
def user_detail(id: int, db: Session = Depends(get_db)):
    my_user = db.query(models.User).get(id)

    if my_user:
        return my_user

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exists")

