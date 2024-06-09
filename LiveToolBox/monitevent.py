import asyncio
import aiohttp
from aiohttp import ClientConnectorError
from PySide6.QtCore import QThread, Signal


class LxSSEThread(QThread):
    data_updated = Signal(str)

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.process_data())

    async def get_data(self):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get("http://localhost:23330/subscribe-player-status") as response:
                    while True:
                        line = await response.content.readline()
                        event = str(line.decode('utf-8').strip())

                        yield event
            except ClientConnectorError:
                event = '无法连接播放器 : 请确认已打开LX播放器后重新开启歌词窗口'
                yield event

    async def process_data(self):
        async for event in self.get_data():
            self.data_updated.emit(event)
