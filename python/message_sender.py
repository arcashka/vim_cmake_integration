import asyncio
import argparse

#parser = argparse.ArgumentParser(description='Send message to cmake server')
#parser.add_argument('message', metavar='message', type=str, nargs=1, help='message to send')

#args = parser.parse_args()
#print(args.message)


async def send_message(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    writer.write(message.encode())

#asyncio.run()
