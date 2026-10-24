from fastapi import FastAPI

app = FastAPI(
    title="Freelance Calculator",
    description="API для расчёта стоимости фриланс-заказов",
    version="1.0.0"
)


@app.get("/")
async def home():
    return {"message": "Привет! FastAPI работает."}

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}
