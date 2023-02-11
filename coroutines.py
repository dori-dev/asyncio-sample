import asyncio
from datetime import datetime


async def say_hello(name: str):
    await asyncio.sleep(2)
    print(f'Hello, {name.title()}!')


async def main():
    jack = asyncio.create_task(say_hello('jack'))
    john = asyncio.create_task(say_hello('john'))
    await jack, john


start = datetime.now()
asyncio.run(main())
end = datetime.now()

print(end - start)
