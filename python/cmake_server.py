import asyncio
from settings import Settings
from cmake_helper import CMakeHelper


quit_message = 'quit'
configure = 'configure'


class Server:
    def __init__(self):
        self.settings = Settings()
        self.settings.parse("vim_cmake_settings.json")
        self.cmake = CMakeHelper()

    async def start(self):
        self.server = await asyncio.start_server(self.handler, '127.0.0.1', 65001)
        async with self.server:
            await self.server.wait_closed()

    async def handler(self, reader, writer):
        data = await reader.read()
        message = data.decode()
        print('got message={}'.format(message))
        if message == quit_message:
            self.server.close()
            writer.feed_eof()
        if message == configure:
            await self.cmake.configure(self.settings.data[0], writer)
        await writer.drain()
        writer.close()


if __name__ == '__main__':
    server = Server()
    asyncio.run(server.start())

