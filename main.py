import asyncio
import aiofiles
import datetime


async def chat_reader():
    while True:
        reader, writer = await asyncio.open_connection(
            'minechat.dvmn.org',
            5000,
        )
        data = await reader.readline()
        datetime_now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
        message = f'[{datetime_now}] {data.decode()}'
        async with aiofiles.open('log.txt', 'a') as f:
            await f.write(message)

        print(message)


if __name__ == '__main__':
    asyncio.run(chat_reader())
