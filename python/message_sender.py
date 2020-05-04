import asyncio
import argparse


class MessageSender:
    async def send(self, message):
        reader, writer = await asyncio.open_connection('127.0.0.1', 65001)
        writer.write(message.encode())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send message to cmake server')
    parser.add_argument('message', metavar='message', type=str, nargs=1, help='message to send')

    args = parser.parse_args()
    print(args.message)

    message_sender = MessageSender()
    asyncio.run(message_sender.send(args.message[0]))

