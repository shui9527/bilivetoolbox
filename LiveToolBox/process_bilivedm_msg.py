class ProcessBilivedmMsg():

    def __init__(self, username, danmaku):
        self.username = username
        self.danmaku = danmaku
        self.order = ''
        self.song_name = ''
        self.song_singer = ''
        self.song_url = ''
        self.date = {'order': '', 'username': username, 'danmaku': danmaku, 'name': '', 'singer': ''}

    def danmaku_handler(self, danmaku):

        danmakulist = danmaku.lstrip().split(' ')
        danmakulist = [i for i in danmakulist if i != '']

        if danmakulist[0] == '点歌' or '切歌':
            self.order = danmakulist[0]
            long = len(danmakulist)
            if 2 <= long:
                self.song_name = danmakulist[1]
                if long >= 3:
                    self.song_singer = danmakulist[2]
            self.date['order'] = self.order
            self.date['name'] = self.song_name
            self.date['singer'] = self.song_singer
            return self.date

        if danmakulist[0] == '排队':
            self.date['order'] = '排队'
            return self.date

# 测试
# username = "shuis"
# danmaku = "  点歌  光年之外  刘德华 张学友"
# danmaku2 =  danmaku.lstrip().split(' ')
# print(danmaku2)
# # danmaku = "切歌"
# pbm = ProcessBilivedmMsg(username, danmaku)
# print(pbm.danmaku_handler(danmaku))
# print(pbm.date)
