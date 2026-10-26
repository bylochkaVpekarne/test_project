from fastapi import FastAPI

import uvicorn

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": {item_id}}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)


# Чупапи пуняню