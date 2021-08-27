from dotenv import load_dotenv
import asyncio
import argparse
import logging
import json
import os


async def sender(args):
    reader, writer = await asyncio.open_connection(args.host, args.port)

    data = await reader.readline()
    log_msg = data.decode()
    logger.debug(log_msg)

    writer.write(f'{args.token}\n'.encode())
    await writer.drain()

    data = await reader.readline()
    log_msg = data.decode()
    if json.loads(log_msg) is None:
        log_msg = 'Неизвестный токен. Проверьте его или зарегистрируйте заново.'
    logger.debug(log_msg)

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
    parser.add_argument('--logger', help='Enable logger', action='store_true')
    parser.add_argument('--message', type=str, help='Message to send to chat.',
        default='Здравствуйте! Я тестирую чатик.')
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('sender')
    logger.disabled = not args.logger

    asyncio.run(sender(args))
