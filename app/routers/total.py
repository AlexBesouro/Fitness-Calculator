import datetime
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app import models, schemas
from sqlalchemy import cast, Date
from sqlalchemy.dialects.postgresql import insert

# Create a router for operations with 'users' request
router = APIRouter(prefix="/total", tags=["total"])
date_today = datetime.date.today()


# Request to calculate total daily tdee
@router.get("/{user_id}", status_code=201)
def total_tdee(user_id: int, db: Session = Depends(get_db)):

    total_calories_eaten_query = (db.query(models.CaloriesConsumptions.eaten_calories_number)
                                  .filter(models.CaloriesConsumptions.user_id == user_id)
                                  .filter(cast(models.CaloriesConsumptions.eaten_calories_created_at, Date) == date_today)
                                  .all())
    total_calories_eaten = list(map(lambda x: x._mapping, total_calories_eaten_query))

    calorie_eaten_result = sum([i["eaten_calories_number"] for i in total_calories_eaten])

    total_calories_burned_query = (db.query(models.BurnedCalories.burned_calories_number)
                                  .filter(models.BurnedCalories.user_id == user_id)
                                  .filter(cast(models.BurnedCalories.created_at, Date) == date_today)
                                  .all())
    total_calories_burned = list(map(lambda x: x._mapping, total_calories_burned_query))

    calorie_burned_result = sum([i["burned_calories_number"] for i in total_calories_burned])

    daily_tdee = calorie_eaten_result - calorie_burned_result


    total_query = (insert(models.Total).values(user_id=user_id, total_calories_eaten=calorie_eaten_result,
                                       total_calories_burned=calorie_burned_result, daily_tdee=daily_tdee)
                                .on_conflict_do_update(index_elements=['user_id', "created_at"],
                                                       set_={'total_calories_eaten': calorie_eaten_result,
                                                             'total_calories_burned': calorie_burned_result,
                                                             'daily_tdee': daily_tdee}))

    db.execute(total_query)

    db.commit()
    return "success"
