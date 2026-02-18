from fastapi import FastAPI

from .database import Base, engine
from .routes import auth, me

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auth API")


app.include_router(auth.router)
app.include_router(me.router)