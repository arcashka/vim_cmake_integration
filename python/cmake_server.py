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
        self.server = await asyncio.start_server(self.handler, '127.0.0.1', 8888)
        async with self.server:
            await self.server.wait_closed()

    async def handler(self, reader, writer):
        data = await reader.read(100)
        message = data.decode()
        if message == quit_message:
            self.server.close()
        if message == configure:
            self.cmake.configure(self.settings.data[0])
        addr = writer.get_extra_info('peername')

        print(f"Received {message!r} from {addr!r}")

        print(f"Send: {message!r}")
        writer.write(data)
        await writer.drain()

        print("Close the connection")
        writer.close()


async def main():
    a = Server()
    await a.start()


asyncio.run(main())
