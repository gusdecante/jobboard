from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base_class import Base
from apis.version1.route_users import router

def create_table():
  Base.metadata.create_all(bind=engine)

def start_application():
  app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
  create_table()
  app.include_router(router)
  return app

app = FastAPI(title=settings.PROJECT_TITLE, varion=settings.PROJECT_VERSION)

@app.get("/")
def hello_api():
  return {"detail": "Hello World!"}