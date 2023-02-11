import asyncio
from asyncio import TimeoutError
from datetime import datetime


async def say_hello():
    await asyncio.sleep(5)
    print('Hello')


async def main():
    task = asyncio.create_task(say_hello())
    try:
        shielded_task = asyncio.shield(task)
        await asyncio.wait_for(shielded_task, timeout=3)
    except TimeoutError:
        print('It took too long to do task...')
        await task
    if task.cancelled():
        print('Task cancelled!')


start = datetime.now()
asyncio.run(main())
end = datetime.now()

print(end - start)
