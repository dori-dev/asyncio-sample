import asyncio


async def run(command, *args):
    process = await asyncio.create_subprocess_exec(
        command,
        *args,
    )
    return await process.wait()


async def main():
    result = await asyncio.gather(
        run('ls'),
        run('sleep', '1'),
        run('echo', 'hello'),
    )
    return result

result = asyncio.run(main())
for item in result:
    print(item)
