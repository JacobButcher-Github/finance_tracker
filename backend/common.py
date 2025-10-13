from collections.abc import Sequence
from typing import Any

import psycopg2
from psycopg2 import extensions
from psycopg2.extras import RealDictCursor


def get_postgres_connection() -> extensions.connection:
    connection = psycopg2.connect(
        "dbname='finances-postgres' user='postgres' host='localhost' password='password'"
    )  # name might be postgres, we'll find out
    connection.autocommit = True  # execute queries immediately
    return connection


def database_execut(
    db: extensions.connection, query: str, args: Sequence[Any] | None = None
) -> None:
    with db.cursor() as cur:
        cur.execute(query, args)


def database_fetch(
    db: extensions.connection,
    query: str,
    args: Sequence[Any] | None = None,
):
    with db.cursor() as cur:
        cur.execute(query, args)
        for record in cur:
            yield record
