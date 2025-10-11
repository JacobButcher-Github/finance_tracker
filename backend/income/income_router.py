from fastapi import APIRouter

income_router = APIRouter()


@income_router.get("/income/")
async def get_income(): ...


@income_router.post("/income/add")
async def update_income(): ...
