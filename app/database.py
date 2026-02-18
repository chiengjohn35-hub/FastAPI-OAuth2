from sqlalchemy import create_engine, engine
from sqlalchemy.orm import declarative_base, sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./auth.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})

SessionLocal = sessionmaker( autoflush=False,autocommit=False, bind=engine)

Base = declarative_base()


#dependency injection for our database

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

