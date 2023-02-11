import asyncio


async def say_hello(name):
    await asyncio.sleep(2)
    print(f"Hello {name}!")


async def main():
    amir = asyncio.create_task(say_hello('amir'))
    mohammad = asyncio.create_task(say_hello('mohammad'))
    await amir, mohammad

loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.close()
