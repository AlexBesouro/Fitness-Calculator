from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app import models

# Create a router for operations with 'users' request
router = APIRouter(prefix="/bmis", tags=["bmis"])


# Request to calculate body mass index
@router.post("/{user_id}")
def calculate_bmi(user_id: int, db: Session = Depends(get_db)):

    user_query = db.query(models.User).filter(models.User.user_id == user_id)
    user = user_query.first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    bmi_number = (1.3 * user.weight) / (user.height / 100) ** 2.5

    bmi_query = models.Bmi(bmi_number=bmi_number, user_id=user_id)
    db.add(bmi_query)
    db.commit()
    db.refresh(bmi_query)
    return {"message": bmi_query}