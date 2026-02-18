from .database import Base
from sqlalchemy import  Column, String, Integer, ForeignKey, Boolean, func
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime


class User(Base):
    __tablename__ ="user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False ) #is never plain text.
    is_active = Column(Boolean, default=True) # lets you soft-disable accounts later.


class PasswordReset(Base):
    __tablename__ = "password_resets"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    token = Column(String, unique=True, index=True, nullable=False)
    used = Column(Boolean, default=False) # to prevent reuse of tokens.
    created_at = Column(DateTime(timezone=True), server_default=func.now()) # to track token age for expiration.

