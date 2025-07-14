from fastapi import FastAPI
from typing import List 
from collect import collect_func
from models import DataObj

app = FastAPI()

#app.include_router(employee_router,prefix="/api",tags=["Employee"])

@app.get("/")
def root():
    return {"output":"WELOCOME TO HOME PAGE"}


@app.post("/collect")
def collect(data: DataObj):
    collect_func(data)