import asyncio
import aiohttp
from aiohttp import ClientConnectorError
from PySide6.QtCore import QThread, Signal

class LXSSEThread(QThread):
    data_updated = Signal(str)

    async def get_data(self):
        while True:
            try:
                timeout = aiohttp.ClientTimeout(total=None, sock_connect=5, sock_read=10)  # 设置连接超时为5秒，读取超时为10秒
                async with aiohttp.ClientSession(timeout=timeout) as session:
                    async with session.get("http://localhost:23330/subscribe-player-status") as response:
                        print('连接状态', response.status)

                        while True:
                            line = await response.content.readline()
                            event = str(line.decode('utf-8').strip())
                            yield event
            except aiohttp.ClientConnectorError:
                event = '无法连接播放器 : 请确认已打开LX播放器'
                yield event
                await asyncio.sleep(5)  # 等待5秒后尝试重新连接

    async def send_data(self):
        async for event in self.get_data():
            self.data_updated.emit(event)

    async def stop(self):
        # 取消请求
        for task in asyncio.all_tasks():
            task.cancel()

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(self.send_data())
        except asyncio.CancelledError:
            pass

    def stop_process(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.stop())
