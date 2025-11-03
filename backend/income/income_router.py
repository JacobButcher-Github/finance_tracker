# STL
from collections.abc import Sequence
from datetime import date, datetime

# UV/PDM
import asyncpg
from asyncpg import Connection
from fastapi import APIRouter, Depends, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# LOCAL
from common import get_postgres_connection
from schemas.income import Income

from .income import delete, get_many, get_one, insert

income_router = APIRouter()


@income_router.get("/income/")
async def get_income(db: Connection = Depends(get_postgres_connection)):
    # TODO: this definitely needs to change. We need to get the *last* months info.
    # Or potentially even multiple depending on user settings. This is a placeholder,
    # but might just make it call the get endpoint with however many months the user has loaded.
    now: date = datetime.now().date()
    results = await get_one(db, now)
    return JSONResponse(content=jsonable_encoder(results))


@income_router.get("/income/get")
async def get_many_income(
    dates: Sequence[date] = Query(...),
    db: Connection = Depends(get_postgres_connection),
):
    results = await get_many(db, dates)
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
