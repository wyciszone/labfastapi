from fastapi import FastAPI
from pydantic import BaseModel

class StudentCreateScheme(BaseModel):
    first_name : str
    last_name :str
app = FastAPI()


@app.get("/items/")
async def create_student(item: StudentCreateScheme):
    return item

