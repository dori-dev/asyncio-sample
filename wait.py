from datetime import datetime
import asyncio
import aiohttp


urls = {
    'https://en.wikipedia.org/wiki/Main_Page': 3,
    'https://en.wikipedia.org/wiki/Python': 9,
    'https://docs.aiohttp.org/en/stable/': 5,
    'https://github.com/aio-libs/aiohttp': 1,
    'https://notexistsdomain32556.dsf': 6,
}


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
            asyncio.create_task(show_status(session, url, delay))
            for url, delay in urls.items()
        ]
        done, pending = await asyncio.wait(
            requests,
            return_when=asyncio.FIRST_EXCEPTION,
        )
        for request in done:
            if request.exception() is None:
                url, status_code = request.result()
                print(f'{url}: {status_code}')
        for request in pending:
            request.cancel()
        print(f"\nTask does not done: {len(pending)} tasks")


start = datetime.now()
asyncio.run(main())
end = datetime.now()

print(f"Get result in {end - start}")
