from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):  #объявляем класс для работы pydantic
    title: str

@app.post("/task") #просто хендлер для получения и возврата данных, в данном случае задачи
def create_task(task: Task):
    return {"Message": f"Задача '{task.title}' получена"}
