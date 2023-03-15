import motor.motor_asyncio
from dotenv import load_dotenv
from bson import ObjectId
from pydantic import BaseModel, Field, EmailStr
import os

# load env
load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL"))

db = client.blog_api

#BSON to JSON
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)
    
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")



class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        allowed_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
            "name": "John Doe",
            "email": "jdoe@example.com",
            "password": "secret_code"
        }
        }
class UserResponse(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
   

    class Config:
        allowed_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
            "name": "John Doe",
            "email": "jdoe@example.com"
            
        }
        }

class BlogContent(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    body: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
            "title": "Blog title",
            "body": "Blog content"
        }
        }


class BlogContentResponse(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    body: str = Field(...)
    author_name: str = Field(...)
    author_id: str = Field(...)
    created_at: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
            "title": "Blog title",
            "body": "Blog content",
            "author_name": "Name of auther",
            "author_id": "Id of author",
            "created_at": "Date of creation"
         
        }
        }


class TokenData(BaseModel):
    id: str


class PasswordReset(BaseModel):
    email: EmailStr

class NewPassword(BaseModel):
    password: str