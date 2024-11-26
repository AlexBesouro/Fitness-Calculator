from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app import models, schemas

# Create a router for operations with 'users' request
router = APIRouter(prefix="/bc", tags=["burned calories"])


# Request to calculate  total daily energy expenditure
@router.post("/{user_id}")
def calculate_burned_calories(user_id: int, exercise: schemas.Exercise, db: Session = Depends(get_db)):

    user_query = db.query(models.User).filter(models.User.user_id == user_id)
    user = user_query.first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    exercise_met_query = db.query(models.Exercises.exercise_met).filter(models.Exercises.exercise_name == exercise.exercise_name).scalar()
    if not exercise_met_query:
        raise HTTPException(status_code=404, detail="Exercise not found")

    burned_calories_number = (exercise_met_query * 3.5 * user.weight * exercise.exercise_time) / 200


    burned_calories_query = models.BurnedCalories(exercise_name=exercise.exercise_name,
                                             burned_calories_number=burned_calories_number, user_id=user_id,
                                             exercise_time= exercise.exercise_time, exercise_met=exercise_met_query)

    db.add(burned_calories_query)
    db.commit()
    db.refresh(burned_calories_query)
    return {"message": burned_calories_number}