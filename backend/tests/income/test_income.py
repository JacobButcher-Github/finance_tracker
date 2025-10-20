# STL
from datetime import date

# PDM/UV
import pytest
from asyncpg import Connection
from httpx import AsyncClient

# LOCAL
from schemas.income import Income

# TODO: Add playwright to this once frontend integration is in


@pytest.mark.asyncio
async def test_income_crud_sequence(client: AsyncClient, db_connection: Connection):
    # Create a test Income
    test_income = Income(
        date=date(2025, 10, 15),
        gross=10.10,
        k401=3.09,
        fed_tax=3.09,
        ss_tax=1.50,
        medicare_tax=0.30,
        state_tax=0.24,
        other_income=1.26,
        net_income=1.32,
        total_tax=2.79,
        tax_percent_income=2.56,
    )
    # Insert
    response = await client.post("/income/insert", json=test_income.model_dump())
    assert response.status_code == 200

    # Get
    response = await client.get("/income/get", params=[("dates", "2025-10-15")])
    assert response.status_code == 200
    data: list[dict[str, date | float]] = response.json()
    assert data[0] == test_income.model_dump()

    # Update
    # Not implemented yet

    # Delete
    response = await client.post("income/delete", params=[("dates", "2025-10-15")])
    assert response.status_code == 200
    query = """
        SELECT *
        FROM income
        WHERE DATE_TRUNC('month', date) = DATE_TRUNC('month', $1::date)
    """
    db_check: list[dict[str, date | float]] = await db_connection.fetch(
        query, (date(2025, 10, 15),)
    )
    assert db_check == []
