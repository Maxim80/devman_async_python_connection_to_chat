from dotenv import load_dotenv
import asyncio
import argparse
import logging
import aiofiles
import json
import os
import re

async def read_data(reader):
    data = await reader.readline()
    data = data.decode()
    logger.debug(data)
    return data


async def register(host, port, nickname):
    try:
        reader, writer = await asyncio.open_connection(host, port)

        await read_data(reader)

        writer.write('\n'.encode())
        await writer.drain()

        await read_data(reader)

        writer.write(f'{nickname}\n'.encode())
        await writer.drain()

        access_data = await read_data(reader)
        async with aiofiles.open('.minechat_access', 'w') as f:
            await f.write(access_data)

    finally:
        writer.close()
        await writer.wait_closed()


async def authorise(reader, writer):
    await read_data(reader)

    try:
        async with aiofiles.open('.minechat_access', 'r') as f:
            data = await f.read()

    except FileNotFoundError:
        print('Вы не авторизованы. Отправлять сообщения в чат могут только авторизованные пользователи')
        return

    access_token = json.loads(data)['account_hash']

    writer.write(f'{access_token}\n'.encode())
    await writer.drain()

    msg = await read_data(reader)
    if json.loads(msg) is None:
        print('Неизвестный токен. Проверьте его или зарегистрируйте заново.')


async def submit_message(reader, writer, message):
    writer.write(f'{message}\n\n'.encode())
    await writer.drain()


async def main(args):
    if args.reg:
        await register(args.host, args.port, args.reg)

    try:
        reader, writer = await asyncio.open_connection(args.host, args.port)
        await authorise(reader, writer)
        message = args.message.replace('\\n', '')
        await submit_message(reader, writer, message)
    finally:
        writer.close()
        await writer.wait_closed()


if __name__ == '__main__':
    load_dotenv()

    parser = argparse.ArgumentParser(description='Script to connection to chats')
    parser.add_argument('-m', '--message',type=str, help='Message for submit',
        required=True)
    parser.add_argument('-H', '--host', type=str, default='minechat.dvmn.org',
        help='IP or URL hosts address for connection.')
    parser.add_argument('-p', '--port', type=int, default=5050,
        help='Port for connection.')
    parser.add_argument('-r', '--reg', type=str,
        help='New user registration name')
    parser.add_argument('-l', '--logger', help='Enable logger',
        action='store_true')
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('sender')
    logger.disabled = not args.logger

    asyncio.run(main(args))
