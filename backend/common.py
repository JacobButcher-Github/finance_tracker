# STL
import os
from collections.abc import AsyncGenerator, Sequence
from typing import Any

# UV/PDM
import asyncpg
from asyncpg import Connection


async def get_postgres_connection() -> Connection:
    """
    Create and return an async PostgreSQL connection.
    """
    # TODO: Convert this to use db_pool, asyncpg has built-ins for it.
    db_url = os.getenv("DATABASE_URL")
    if db_url is None:
        raise RuntimeError("DATABASE_URL is not set")
    connection: asyncpg.Connection = await asyncpg.connect(dsn=db_url)
    return connection


async def database_execute(
    db: Connection, query: str, args: Sequence[Any] | None = None
) -> None:
    """
    Execute a query (INSERT/UPDATE/DELETE) without returning results.
    """
    if args is None:
        _ = await db.execute(query)
    else:
        _ = await db.execute(query, *args)


async def database_fetch(
    db: Connection, query: str, args: Sequence[Any] | None = None
) -> list[dict[str, Any]]:
    """
    Execute a SELECT query and yield each record asynchronously.
    """
    if args is None:
        records = await db.fetch(query)
    else:
        records = await db.fetch(query, *args)
    return [dict(r) for r in records]
