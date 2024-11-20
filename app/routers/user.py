from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app import models

# Create a router for operations with 'users' request
router = APIRouter(prefix="/users", tags=["users"])

# Request to find a user by id
@router.get("/{user_id}")
def find_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.user_id == user_id)
    user_to_find = user_query.first()
    if not user_to_find:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message" : user_to_find}
