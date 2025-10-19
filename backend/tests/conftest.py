# STL
import asyncio
import os

# PDM/UV
import asyncpg
import pytest
from asyncpg import Connection
from httpx import AsyncClient

# LOCAL
from app import app
from common import get_postgres_connection

TEST_DATABASE_URL = "postgresql://postgres:password@localhost:5432/finances_test"


@pytest.fixture(scope="session")
def event_loop():
    """Ensure pytest-asyncio uses a session-wide event loop."""
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def test_db():
    """Create and teardown a clean test database."""
    conn = await asyncpg.connect(TEST_DATABASE_URL)
    _ = await conn.execute("DROP SCHEMA finances CASCADE; CREATE SCHEMA finances;")
    yield conn
    await conn.close()


@pytest.fixture()
async def db_connection():
    """Return a fresh connection for each test."""
    # TODO: Update this to support pools
    conn = await asyncpg.connect(TEST_DATABASE_URL)
    yield conn
    await conn.close()


@pytest.fixture()
async def client(db_connection: Connection):
    """Provide a FastAPI test client that uses the test DB."""

    async def _get_test_db():
        yield db_connection

    app.dependency_overrides[get_postgres_connection] = _get_test_db
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
