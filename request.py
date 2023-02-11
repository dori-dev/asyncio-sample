from datetime import datetime
import asyncio
import aiohttp

urls = [
    'https://en.wikipedia.org/wiki/Main_Page',
    'https://en.wikipedia.org/wiki/Python',
    'https://en.wikipedia.org/wiki/Python_(programming_language)',
    'https://en.wikipedia.org/wiki/Django_(web_framework)',
    'https://en.wikipedia.org/wiki/HTTP_cookie',
    'https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol',
    'https://en.wikipedia.org/wiki/HTTPS',
    'https://en.wikipedia.org/wiki/HTTP_404',
    'https://docs.aiohttp.org/en/stable/',
    'https://github.com/aio-libs/aiohttp',
    'https://notexistsdomain32556.dsf',
]


async def show_status(session: aiohttp.client.ClientSession, url):
    try:
        async with session.get(url) as response:
            return url, response.status
    except Exception:
        return url, 0


async def main():
    async with aiohttp.ClientSession() as session:
        requests = [
            show_status(session, url)
            for url in urls
        ]
        return await asyncio.gather(*requests, return_exceptions=False)


start = datetime.now()
for url, status_code in asyncio.run(main()):
    print(f"{url}: {status_code}")
end = datetime.now()

print(f"\nGet result in {end - start}")
