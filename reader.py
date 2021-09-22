import asyncio
import aiofiles
import datetime
import argparse


async def reader(args):
    try:
        reader, writer = await asyncio.open_connection(args.host, args.port)
        while True:
            chat_mesage = await reader.readline()
            datetime_now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
            press_release = f'[{datetime_now}] {chat_mesage.decode()}'
            async with aiofiles.open(args.history, 'a') as f:
                await f.write(press_release)

            print(press_release)
    finally:
        writer.close()
        await writer.wait_closed()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script to connection to chats')
    parser.add_argument('-H', '--host', type=str, default='minechat.dvmn.org',
        help='IP or URL hosts address for connection.')
    parser.add_argument('-p', '--port', type=int, default=5000,
        help='Port for connection.')
    parser.add_argument('--history', type=str, default='./minechat.history',
        help='Path to the file with the history of correspondence.')
    args = parser.parse_args()
    asyncio.run(reader(args))
