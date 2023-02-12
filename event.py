import asyncio
import functools


def trigger_event(event: asyncio.locks.Event):
    event.set()


async def do_work_on_event(event: asyncio.locks.Event):
    print('Waiting for event...')
    await event.wait()
    print('Performing work...')
    await asyncio.sleep(3)
    print('Finished work!')
    event.clear()


async def main():
    event = asyncio.Event()
    trigger_event_func = functools.partial(trigger_event, event)
    asyncio.get_event_loop().call_later(
        1, trigger_event_func
    )
    await asyncio.gather(
        do_work_on_event(event),
        do_work_on_event(event),
        do_work_on_event(event),
    )


asyncio.run(main())
