from PySide6.QtCore import QThread
import asyncio
import blivedm
import blivedm.models.open_live as open_models
from process_bilivedm_msg import ProcessBilivedmMsg


class MyHandler(blivedm.BaseHandler):
    def __init__(self, callbackfunc):
        self.callbackfunc = callbackfunc

    # def _on_heartbeat(self, client: blivedm.BLiveClient, message: web_models.HeartbeatMessage):
    #     print(f'[{client.room_id}] 心跳')

    def _on_open_live_danmaku(self, client: blivedm.OpenLiveClient, message: open_models.DanmakuMessage):
        # print(f'[{message.room_id}] {message.uname}：{message.msg}')
        pbm = ProcessBilivedmMsg(message.uname, message.msg)
        date = pbm.danmaku_handler(message.msg)
        self.callbackfunc(date)

    def _on_open_live_gift(self, client: blivedm.OpenLiveClient, message: open_models.GiftMessage):
        coin_type = '金瓜子' if message.paid else '银瓜子'
        total_coin = message.price * message.gift_num
        print(f'[{message.room_id}] {message.uname} 赠送{message.gift_name}x{message.gift_num}'
              f' （{coin_type}x{total_coin}）')

    def _on_open_live_buy_guard(self, client: blivedm.OpenLiveClient, message: open_models.GuardBuyMessage):
        print(f'[{message.room_id}] {message.user_info.uname} 购买 大航海等级={message.guard_level}')

    def _on_open_live_super_chat(
            self, client: blivedm.OpenLiveClient, message: open_models.SuperChatMessage
    ):
        print(f'[{message.room_id}] 醒目留言 ¥{message.rmb} {message.uname}：{message.message}')

    def _on_open_live_super_chat_delete(
            self, client: blivedm.OpenLiveClient, message: open_models.SuperChatDeleteMessage
    ):
        print(f'[{message.room_id}] 删除醒目留言 message_ids={message.message_ids}')

    def _on_open_live_like(self, client: blivedm.OpenLiveClient, message: open_models.LikeMessage):
        print(f'[{message.room_id}] {message.uname} 点赞')


class BiliClientThread(QThread):

    # data_updated = Signal(str)

    def __init__(self, parent=None, room_code=None, callbackfunction=None):
        super(BiliClientThread, self).__init__(parent)
        self.room_code = room_code
        self.callbackfunction = callbackfunction

    def get_code(self, code):
        self.room_code = code

    def run(self):

        asyncio.run(self.get_data(self.room_code))

    def stop(self):
        self.stopped = True  # 设置标志为 True，表示线程应该停止

    async def get_data(self, code):

        # 在开放平台申请的开发者密钥
        ACCESS_KEY_ID = '6VNwGnsiD7gS7EIKf724i73W'
        ACCESS_KEY_SECRET = 'Oh4qjLMiY4G1q51QxVHJTKMau1eTbn'
        # 在开放平台创建的项目ID
        APP_ID = 1721347633961
        # 主播身份码
        ROOM_OWNER_AUTH_CODE = code

        # 创建客户端
        client = blivedm.OpenLiveClient(
            access_key_id=ACCESS_KEY_ID,
            access_key_secret=ACCESS_KEY_SECRET,
            app_id=APP_ID,
            room_owner_auth_code=ROOM_OWNER_AUTH_CODE,
        )
        handler = MyHandler(self.callbackfunction)

        client.set_handler(handler)

        client.start()

        try:
            # 演示70秒后停止
            # await asyncio.sleep(70)
            # client.stop()

            await client.join()
        finally:
            await client.stop_and_close()
