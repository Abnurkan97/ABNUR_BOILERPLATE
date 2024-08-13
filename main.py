import logging
from fastapi import FastAPI
from api.db.database import engine,SQLALCHEMY_DATABASE_URL,create_tables,check_database_connection

from api.v1 import models
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from api.v1.routes import api_version_one

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.include_router(api_version_one)




@app.on_event("startup")
async def on_startup():
    if check_database_connection():
        logging.info("Database is connected succesfully.")
        create_tables()
    else:
        logging.error("Database connection failed.")

@app.get("/")
async def read_root():
    return {"message": "welcome to ABNURKHAN API BOILERPLATE"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
