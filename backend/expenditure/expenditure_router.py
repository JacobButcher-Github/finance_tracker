# STL
from collections.abc import Sequence
from datetime import date, datetime

# UV/PDM
from asyncpg import Connection
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# LOCAL
from common import get_postgres_connection
from schemas.expenditure import Expenditure

from .expenditure import delete, get_many_date, get_one_date, insert

expenditure_router = APIRouter()


@expenditure_router.get("/expenditure/")
async def get_expenditure(db: Connection = Depends(get_postgres_connection)):
    # TODO: this definitely needs to change. We need to get the *last* months info.
    # Or potentially even multiple depending on user settings. This is a placeholder,
    # but might just make it call the get endpoint with however many months the user has loaded.
    now: date = datetime.now().date()
    results = await get_one_date(db, now)
    return JSONResponse(content=jsonable_encoder(results))


@expenditure_router.get("expenditure/get")
async def get_many_expenditure(
    dates: Sequence[date], db: Connection = Depends(get_postgres_connection)
):
    results = await get_many_date(db, dates)
    return JSONResponse(content=jsonable_encoder(results))


@expenditure_router.post("/expenditure/insert")
async def insert_expenditure(
    expenditure: Expenditure, db: Connection = Depends(get_postgres_connection)
):
    expenditure_dict = expenditure.model_dump()
    await insert(db, expenditure_dict)
    return {"message": "Expenditure inserted succesfully"}


@expenditure_router.post("/expendiutre/delete")
async def delete_expenditure(
    date: date, db: Connection = Depends(get_postgres_connection)
):
    await delete(db, date)
    return {"message": "Expenditure deleted succesfully"}
