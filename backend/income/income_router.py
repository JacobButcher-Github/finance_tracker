# STL
from datetime import date, datetime

# UV/PDM
import asyncpg
from asyncpg import Connection
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# LOCAL
from common import get_postgres_connection
from schemas.income import Income

from .income import delete, get, insert

income_router = APIRouter()


@income_router.get("/income/")
async def get_income(db: Connection = Depends(get_postgres_connection)):
    # this probably needs to change. We need to get the *last* months info.
    now: date = datetime.now().date()
    results = await get(db, now)
    return JSONResponse(content=jsonable_encoder(results))


@income_router.post("/income/insert")
async def insert_income(
    income: Income, db: Connection = Depends(get_postgres_connection)
):
    income_dict = income.model_dump()
    await insert(db, income_dict)
    return {"message": "Income inserted succesfully"}


@income_router.post("/income/add")
async def update_income(db: Connection = Depends(get_postgres_connection)): ...


@income_router.post("/income/delete")
async def delete_income(date: date, db: Connection = Depends(get_postgres_connection)):
    await delete(db, date)
