# STL
from datetime import datetime

# UV/PDM
import aiopg
from aiopg.connection import Connection
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from psycopg2.extras import RealDictCursor

# LOCAL
from ..common import get_postgres_connection
from ..schemas.income import Income
from .income import get, insert

income_router = APIRouter()


@income_router.get("/income/")
async def get_income(db: Connection = Depends(get_postgres_connection)):
    # this probably needs to change. We need to get the *last* months info.
    now = datetime.now()
    date_str = now.strftime("%Y-%m")
    results = await get(db, date_str)
    return JSONResponse(content=jsonable_encoder(results))


@income_router.post("income/insert")
async def insert_income(
    income: Income, db: Connection = Depends(get_postgres_connection)
):
    income_dict = income.model_dump()
    await insert(db, income_dict)
    return {"message": "Income inserted succesfully"}


@income_router.post("/income/add")
async def update_income(db: Connection = Depends(get_postgres_connection)): ...
