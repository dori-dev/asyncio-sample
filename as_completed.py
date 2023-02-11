from datetime import datetime
import asyncio
import aiohttp


async def show_status(session: aiohttp.client.ClientSession, url, delay):
    await asyncio.sleep(delay)
    try:
        async with session.get(url) as response:
            status_code = response.status
    except Exception:
        status_code = 0
    return url, status_code


async def main():
    async with aiohttp.ClientSession() as session:
        requests = [
            show_status(session, 'https://en.wikipedia.org/wiki/Main_Page', 3),
            show_status(session, 'https://en.wikipedia.org/wiki/Python', 9),
            show_status(session, 'https://docs.aiohttp.org/en/stable/', 5),
            show_status(session, 'https://github.com/aio-libs/aiohttp', 1),
            show_status(session, 'https://notexistsdomain32556.dsf', 6),
        ]
        for request in asyncio.as_completed(requests):
            url, status_code = await request
            print(f'{url}: {status_code}')


start = datetime.now()
asyncio.run(main())
end = datetime.now()

print(f"\nGet result in {end - start}")
