from typing import Optional
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app import models, schemas

# Create a router for operations with 'users' request
router = APIRouter(prefix="/foods", tags=["foods"])

# Request to find food by name
@router.get("/")
def find_food_by_name(db: Session = Depends(get_db), search: Optional[str] = ""):
    food_query = db.query(models.Food).filter(models.Food.food_name.contains(search))
    food_to_find = food_query.all()
    if not food_to_find:
        raise HTTPException(status_code=404, detail="Food not found")
    return {"message" : food_to_find}

# Request to create a new suer
@router.post("/", status_code=201)
def add_food(food:schemas.FoodCreate, db: Session = Depends(get_db)):
    food_query = db.query(models.Food).filter(models.Food.food_name == food.food_name).first()
    if food_query:
        raise HTTPException(status_code=409, detail=f"This food is already in our database")
    new_food = models.Food(**food.model_dump())
    db.add(new_food)
    db.commit()
    db.refresh(new_food)  # RETURNING SQLALCHEMY METHOD
    return new_food