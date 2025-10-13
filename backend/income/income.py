# STL
import asyncio
from datetime import datetime
from typing import Any

# UV/PDM
import aiopg
from aiopg.connection import Connection

# LOCAL
from ..common import database_execute, database_fetch


async def insert_income(db: Connection, item: dict[str, float | str]) -> None:
    """
    To be used by income "/add" endpoint to insert given data as a new month
    """
    existing_str = (
        f"SELECT * FROM income WHERE DATE_TRUNC('month', date) = {item["date"]}"
    )
    existing = database_fetch(db, existing_str)

    if existing:
        await multi_field_update_income(db)

    await database_execute(
        db,
        """
        INSERT INTO income (date, gross, k401, fed_tax, ss_tax, medicare_tax, state_tax, other_income, net_income, total_tax, tax_percent_income)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)
        ON CONFLICT (id) DO UPDATE SET
            date = EXCLUDED.date,
            gross = EXCLUDED.gross,
            k401 = EXCLUDED.k401,
            fed_tax = EXCLUDED.fed_tax,
            ss_tax = EXCLUDED.ss_tax,
            medicare_tax = EXCLUDED.medicare_tax,
            state_tax = EXCLUDED.state_tax,
            other_income = EXCLUDED.other_income,
            net_income = EXCLUDED.net_income,
            total_tax = EXCLUDED.total_tax,
            tax_percent_income = EXCLUDED.tax_percent_income 
        """,
        [
            item["date"],
            item["gross"],
            item["k401"],
            item["fed_tax"],
            item["ss_tax"],
            item["medicare_tax"],
            item["state_tax"],
            item["other_income"],
            item["net_income"],
            item["total_tax"],
            item["tax_percent_income"],
        ]
    )
       
async def get_income(db: Connection, date_str: str):
    """
    To be used by the "/" endpoint to return information on income. 
    """
    #TODO: consider that I'm going to use this when also increasing the number of months to view.
    #I guess I need another enpoint?
    #Perhaps get_multiple_income and just make it a different endpoint entirely is also reasonable.

    query = (
        f"SELECT * FROM income WHERE DATE_TRUNC('month', date) = {date_str}"
    )
    return database_fetch(db, query)

async def update_income(db: Connection) -> None:
    ...

async def multi_field_update_income(db: Connection) -> None:
    ...

async def delete_income(db: Connection) -> None:
    ...
