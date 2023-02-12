import asyncio

semaphore = asyncio.BoundedSemaphore(value=4)


async def show():
    async with semaphore:
        print('Show somethings...')
        await asyncio.sleep(0.5)


async def main():
    show_list = [
        show()
        for _ in range(20)
    ]
    await asyncio.gather(*show_list)

asyncio.run(main())
