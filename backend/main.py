from fastapi import FastAPI

import uvicorn

app = FastAPI() #само приложение к которому уже подключаются все нужные данные

@app.get("/items/{item_id}")        #вызывается при обращении к этому адресу
async def read_item(item_id: int):
    return {"item_id": {item_id}}

if __name__ == "__main__":
    print("Запуск")                 
    uvicorn.run("main:app", reload=True)
