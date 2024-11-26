from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app import models

# Create a router for operations with 'users' request
router = APIRouter(prefix="/tdees", tags=["tdees"])


# Request to calculate  total daily energy expenditure
@router.post("/{user_id}")
def calculate_tdee(user_id: int, db: Session = Depends(get_db)):

    user_query = db.query(models.User).filter(models.User.user_id == user_id)
    user = user_query.first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.gender == "male":
        basal_metabolic_rate = 10 * user.weight + 6.25 * user.height - 5 * user.age + 5
    else:
        basal_metabolic_rate = 10 * user.weight + 6.25 * user.height - 5 * user.age - 161

    if user.activity_level == 1:
        tdee_number = basal_metabolic_rate * 1.2
    elif user.activity_level == 2:
        tdee_number = basal_metabolic_rate * 1.375
    elif user.activity_level == 3:
        tdee_number = basal_metabolic_rate * 1.55
    elif user.activity_level == 4:
        tdee_number = basal_metabolic_rate * 1.725
    else:
        tdee_number = basal_metabolic_rate * 1.9

    tdee_query = models.Tdee(tdee_number=tdee_number, user_id=user_id)
    db.add(tdee_query)
    db.commit()
    db.refresh(tdee_query)  # RETURNING SQLALCHEMY METHOD
    return {"message": tdee_query}