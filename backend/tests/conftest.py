# STL
import asyncio

# PDM/UV
import asyncpg
import pytest
import pytest_asyncio
from asyncpg import Connection
from httpx import ASGITransport, AsyncClient

# LOCAL
from app.app import app
from common import get_postgres_connection
from tests.constants import TEST_DATABASE_URL


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
    _ = await conn.execute("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")
    yield conn
    await conn.close()


# async def ensure_test_database():
#     admin_conn = await asyncpg.connect("postgresql://postgres:password@db:5432/postgres")
#     exists = await admin_conn.fetchval(
#         "SELECT 1 FROM pg_database WHERE datname = 'finances_test'"
#     )
#     if not exists:
#         await admin_conn.execute("CREATE DATABASE finances_test;")
#     await admin_conn.close()


@pytest.fixture()
async def db_connection():
    """Return a fresh connection for each test."""
    # TODO: Update this to support pools
    conn = await asyncpg.connect(TEST_DATABASE_URL)
    yield conn
    await conn.close()


@pytest_asyncio.fixture()
async def client(db_connection: Connection):
    """Provide a FastAPI test client that uses the test DB."""

    async def _get_test_db():
        yield db_connection

    app.dependency_overrides[get_postgres_connection] = _get_test_db

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()
