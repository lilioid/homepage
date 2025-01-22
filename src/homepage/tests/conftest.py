import aiohttp
import pytest_asyncio


@pytest_asyncio.fixture
async def http_session():
    async with aiohttp.ClientSession() as session:
        yield session
