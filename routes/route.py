from fastapi import APIRouter
from models.persons import User
from users import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


# GET Request Method
@router.get("/")
async def get_users():
    users = list_serial(collection_name.find())
    return users
