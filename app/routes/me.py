from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..deps import get_current_user
from ..schemas import User as UserSchema

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/me", response_model=UserSchema)
def read_me(current_user = Depends(get_current_user)):
    return current_user

