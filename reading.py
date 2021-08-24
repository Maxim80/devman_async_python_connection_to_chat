import asyncio
import aiofiles
import datetime
import argparse


async def reader(args):
    while True:
        reader, _ = await asyncio.open_connection(args.host, args.port)
        data = await reader.readline()
        datetime_now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
        message = f'[{datetime_now}] {data.decode()}'
        async with aiofiles.open(args.history, 'a') as f:
            await f.write(message)

        print(message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script to connection to chats')
    parser.add_argument('--host', type=str, default='minechat.dvmn.org',
        help='IP or URL hosts address for connection.')
    parser.add_argument('--port', type=int, default=5000,
        help='Port for connection.')
    parser.add_argument('--history', type=str, default='./minechat.history',
        help='Path to the file with the history of correspondence.')
    args = parser.parse_args()
    asyncio.run(reader(args))
