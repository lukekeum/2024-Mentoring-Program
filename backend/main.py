from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
saved_number = 0

origins = [
  '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Save(BaseModel):
  number: int

@app.post("/")
async def save_number(save: Save):
  global saved_number
  save_dict = save.dict()
  saved_number = save_dict['number']
  return { "result": True }

@app.get("/")
async def load_number():
  global saved_number
  return saved_number