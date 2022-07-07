# Python
from datetime import date, datetime
from typing import Optional
from uuid import UUID

# Pydantic
from pydantic import BaseModel, EmailStr, Field

# Fast API
from fastapi import FastAPI
from fastapi import status

app = FastAPI()

# Models
class User(BaseModel):
    user_id : UUID = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
    )
    firstname: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    lastname: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birthdate: Optional[date] = Field(default=None)


class Tweet:
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256,
    )
    create_at: datetime = Field(default=datetime.now())
    update_at: datetime = Field(default=datetime.now())
    by: User = Field(...)


@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=['Home']
)
def home():
    """
    Home
    
    This path operation returns a greeting
    
    Parameters:
    - This path doesn't require any params.

    Returns: application/json: Congrats the user
    """
    return {'Twitter API': 'Working!'}