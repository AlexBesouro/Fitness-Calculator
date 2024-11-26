from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing_extensions import Optional, Literal


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    gender: Literal["male", "female"]
    age: int
    height: int
    weight: float
    activity_level: Literal[1, 2, 3, 4, 5]


class FoodCreate(BaseModel):
    food_name: str
    food_calories: int

class FoodEaten(BaseModel):
    food_name: str
    food_mass: int

class Exercise(BaseModel):
    exercise_name: str
    exercise_time: float
