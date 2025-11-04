# STL
from collections.abc import Sequence
from datetime import date

# UV/PDM
from asyncpg import Connection

# LOCAL
from common import database_execute, database_fetch


async def insert(db: Connection, item: dict[str, float | date | str]) -> None:
    """
    To be used by expenditure "/insert" endpoint to insert given data item.
    Expenditures have ids, and are allowed to duplicate across months unlike the rest of the tables.
    """
    existing_str = """
        SELECT *
        FROM expenditure
        WHERE DATE_TRUNC('month', date) = DATE_TRUNC('month', $1::date) AND
        category = $2 AND 
        amount = $3
    """

    existing = await database_fetch(
        db, existing_str, (item["date"], item["category"], item["amount"])
    )

    if existing:
        await multi_field_update_expenditure(db)

    await database_execute(
        db,
        """
        INSERT INTO expenditure (date, category, amount)
        VALUES ($1, $2, $3)
        ON CONLICT (id) DO UPDATE SET 
            date = EXCLUDED.date,
            category = EXCLUDED.category,
            amount = EXCLUDED.amount
        """,
        [
            item["date"],
            item["category"],
            item["amount"],
        ],
    )


async def get_one_date(db: Connection, date_info: date):
    """
    To be used by the "/" endpoints to return information all expenditures tied to 1 specific date.
    """
    query = """
        SELECT *
        FROM expenditure
        WHERE DATE_TRUNC('month', date) = DATE_TRUNC('month', $1::date)
    """
    return await database_fetch(db, query, (date_info,))


async def get_many_date(db: Connection, date_info: Sequence[date]):
    query = """
        SELECT *
        FROM expenditure
        WHERE DATE_TRUNC('month', date) IN (
            SELECT DATE_TRUNC('month', d::date)
            FROM UNNEST($1::date[]) as d
        )
    """
    return await database_fetch(db, query, date_info)


async def update_expenditure(db: Connection): ...


async def multi_field_update_expenditure(db: Connection): ...


async def delete(db: Connection, date_info: date) -> None:
    query = """
        DELETE *
        FROM expenditure
        WHERE DATE_TRUNC('month', date) = DATE_TRUNC('month', $1::date)
    """
    # TODO: reconsider how this delete should work.
    # Right now it deletes everything associated with that month,
    # probably should make it more individual for how expenditure is laid out

    return await database_execute(db, query, (date_info,))
