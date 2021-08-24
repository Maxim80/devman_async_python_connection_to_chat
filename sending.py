from dotenv import load_dotenv
import asyncio
import argparse
import os


async def sender(args):
    reader, writer = await asyncio.open_connection(args.host, args.port)

    writer.write(f'{args.token}\n'.encode())
    await writer.drain()

    writer.write(f'{args.message}\n\n'.encode())
    await writer.drain()

    writer.close()
    await writer.wait_closed()


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(description='Script to connection to chats')
    parser.add_argument('--host', type=str, default='minechat.dvmn.org',
        help='IP or URL hosts address for connection.')
    parser.add_argument('--port', type=int, default=5050,
        help='Port for connection.')
    parser.add_argument('--token', type=str, default=os.getenv('MINECHAT_ACCESS_TOKEN'),
        help='Minechat access token.')
    parser.add_argument('--message', type=str, help='Message to send to chat.',
        default='Здравствуйте! Я тестирую чатик.')
    args = parser.parse_args()
    asyncio.run(sender(args))
