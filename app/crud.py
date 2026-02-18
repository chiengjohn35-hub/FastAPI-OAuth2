from sqlalchemy.orm import Session
from app.security import get_password_hash
from app.security import get_password_hash
from . import models, security
from .database import get_db
from . import models, security, schemas
from .schemas import UserCreate, User
import secrets



# Get user by email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


#Create user
def create_user(db: Session, user_in: schemas.UserCreate):
    """
        Hashes password.
        Creates and persists user.
        Returns the DB object.
    """
    hashed_password = get_password_hash(user_in.password)
    db_user = models.User( name=user_in.name, email=user_in.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user




# Create password reset token
def create_password_reset(db: Session, email: str):
    """
        Finds user.
        Generates token.
        Saves reset record.
    """
    user = get_user_by_email(db, email)
    if not user:
        return None

    token = secrets.token_urlsafe(24)
    pr = models.PasswordReset(user_id=user.id, token=token)
    db.add(pr)
    db.commit()
    db.refresh(pr)
    return pr

#verify password reset token
def verify_password_reset(db: Session, token: str):
    # Finds reset record by token, ensuring it’s unused.
    return db.query(models.PasswordReset).filter(
        models.PasswordReset.token == token,
        models.PasswordReset.used == False
    ).first()


# Use password reset token to set new password
def use_password_reset(db: Session, token: str, new_password: str):
    """
        Validates token.
        Updates user’s password.
        Marks token as used.
    """
    pr = verify_password_reset(db, token)
    if not pr:
        return None

    user = db.query(models.User).filter(models.User.id == pr.user_id).first()
    user.hashed_password = get_password_hash(new_password)
    pr.used = True

    db.commit()
    db.refresh(user)
    return user
