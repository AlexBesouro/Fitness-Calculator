from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app import models, schemas

# Create a router for operations with 'users' request
router = APIRouter(prefix="/cc", tags=["calories consumption"])


# Request to calculate body mass index
@router.post("/{user_id}")
def add_eaten_calories(user_id: int, food: schemas.FoodEaten, db: Session = Depends(get_db)):

    user_query = db.query(models.User).filter(models.User.user_id == user_id)
    user = user_query.first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    calories_query = db.query(models.Food.food_calories).filter(models.Food.food_name == food.food_name).scalar()
    if not calories_query:
        raise HTTPException(status_code=404, detail="Food is not in our database. You can add it if you want")
    # print(calories_query)
    eaten_calories_number = calories_query * (food.food_mass / 100)

    eaten_food_query =  models.CaloriesConsumptions(user_id=user_id, eaten_food_name=food.food_name,
                                                    eaten_food_mass=food.food_mass,
                                                    eaten_calories_number=eaten_calories_number)
    db.add(eaten_food_query)
    db.commit()
    db.refresh(eaten_food_query)
    return eaten_food_query
