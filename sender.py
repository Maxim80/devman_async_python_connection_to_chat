from dotenv import load_dotenv
import asyncio
import argparse
import logging
import aiofiles
import json
import os


async def read_data(reader):
    data = await reader.readline()
    return data.decode()


async def reg_new_user(host, port, nickname):
    try:
        reader, writer = await asyncio.open_connection(host, port)
        log_msg = await read_data(reader)
        logger.debug(log_msg)

        writer.write('\n'.encode())
        await writer.drain()

        log_msg = await read_data(reader)
        logger.debug(log_msg)

        writer.write(f'{nickname}\n'.encode())
        await writer.drain()

        access_json = await read_data(reader)
        logger.debug(access_json)
        async with aiofiles.open('.minechat_access', 'w') as f:
            await f.write(access_json)

    finally:
        writer.close()
        await writer.wait_closed()


async def main(args):
    if args.reg:
        await reg_new_user(args.host, args.port, 'Bax')
    try:
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
    finally:
        writer.close()
        await writer.wait_closed()


if __name__ == '__main__':
    load_dotenv()

    parser = argparse.ArgumentParser(description='Script to connection to chats')
    parser.add_argument('--host', type=str, default='minechat.dvmn.org',
        help='IP or URL hosts address for connection.')
    parser.add_argument('--port', type=int, default=5050,
        help='Port for connection.')
    parser.add_argument('--reg', help='New user registration',
        action='store_true')
    parser.add_argument('--logger', help='Enable logger', action='store_true')
    parser.add_argument('--message', type=str, help='Message to send to chat.',
        default='')
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('sender')
    logger.disabled = not args.logger

    asyncio.run(main(args))
