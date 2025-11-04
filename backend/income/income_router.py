# STL
from datetime import date, datetime

# UV/PDM
from asyncpg import Connection
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# LOCAL
from common import get_postgres_connection
from schemas.income import Income

from .income import delete, get_many, get_one, insert

income_router = APIRouter()


@income_router.get("/income/get")
async def get_many_income(
    start_date: date = datetime.now().date(),
    end_date: date = datetime.now().date(),
    db: Connection = Depends(get_postgres_connection),
):

    results = await get_many(db, start_date, end_date)
    return JSONResponse(content=jsonable_encoder(results))


@income_router.post("/income/insert")
async def insert_income(
    income: Income, db: Connection = Depends(get_postgres_connection)
):
    income_dict = income.model_dump()
    await insert(db, income_dict)
    return {"message": "Income inserted succesfully"}


@income_router.post("/income/delete")
async def delete_income(date: date, db: Connection = Depends(get_postgres_connection)):
    await delete(db, date)
    return {"message": "Income deleted succesfully"}
