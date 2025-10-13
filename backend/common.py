# STL
from collections.abc import AsyncGenerator, Sequence
from typing import Any

# UV/PDM
import aiopg
from aiopg.connection import Connection
from psycopg2.extras import RealDictCursor


async def get_postgres_connection() -> Connection:
    """
    Create and return an async PostgreSQL connection.
    """
    connection: Connection = await aiopg.connect(
        dbname="finances-postgres",
        user="postgres",
        host="localhost",
        password="password",
        cursor_factory=RealDictCursor,  # rows as dicts
    )  # db name might be postgres, we'll find out
    connection.autocommit = True
    return connection


async def database_execute(
    db: Connection, query: str, args: Optional[Sequence[Any]] = None
) -> None:
    """
    Execute a query (INSERT/UPDATE/DELETE) without returning results.
    """
    async with db.cursor() as cur:
        await cur.execute(query, args)


async def database_fetch(
    db: Connection, query: str, args: Sequence[Any] | None = None
) -> AsyncGenerator[dict[str, Any], None]:
    """
    Execute a SELECT query and yield each record asynchronously.
    """
    async with db.cursor() as cur:
        await cur.execute(query, args)
        async for record in cur:
            yield record
