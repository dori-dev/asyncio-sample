import asyncio

counter = 0

lock = asyncio.Lock()


async def increment():
    global counter
    async with lock:
        temp_counter = counter
        temp_counter += 1
        await asyncio.sleep(0.01)
        counter = temp_counter


async def main():
    tasks = [
        asyncio.create_task(increment())
        for _ in range(100)
    ]
    await asyncio.gather(*tasks)
    print(f"Counter is {counter}")


asyncio.run(main())
