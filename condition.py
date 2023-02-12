import asyncio


async def do_work(condition: asyncio.locks.Condition):
    async with condition:
        print('Locked...')
        await condition.wait()
        print('Event happened...')
        await asyncio.sleep(1)
        print('Work finished.')


async def fire_event(condition: asyncio.locks.Condition):
    await asyncio.sleep(5)
    async with condition:
        print('notifying all tasks...')
        condition.notify_all()
    print('Notification finished.')


async def main():
    condition = asyncio.Condition()
    asyncio.create_task(fire_event(condition))
    await asyncio.gather(
        do_work(condition),
        do_work(condition),
    )

asyncio.run(main())
