# STL
import datetime

# UV/PDM
import psycopg2

# LOCAL
from ..common import database_execute, database_fetch


async def insert_income() -> str:
