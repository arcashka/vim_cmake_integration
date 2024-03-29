import asyncio
import argparse
import vim

from os import path


class MessageSender:
    async def send(self, message):
        reader, writer = await asyncio.open_connection('127.0.0.1', 65001)
        writer.write(message.encode())
        await writer.drain()

        vim.command("botright new")
        vim.command("let w:scratch = 1")
        vim.command("setlocal buftype=nofile bufhidden=wipe nobuflisted noswapfile")
        vim.command("resize 10")
        output_window = vim.current.buffer

        while not reader.at_eof():
            output = await reader.readline()
            output_window.append(output.splitlines())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send message to cmake server')
    parser.add_argument('message', metavar='message', type=str, nargs=1, help='message to send')

    args = parser.parse_args()

    message_sender = MessageSender()
    asyncio.run(message_sender.send(args.message[0]))

