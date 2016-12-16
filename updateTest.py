#coding:utf-8

print("App started")
import time
import datetime
import commands
from slacker import Slacker

date = str(datetime.datetime.today())


class Slack(object):

    __slacker = None

    def __init__(self, token):

        self.__slacker = Slacker(token)

    def get_channnel_list(self):
        """
        Slackチーム内のチャンネルID、チャンネル名一覧を取得する。
        """

        # bodyで取得することで、[{チャンネル1},{チャンネル2},...,]の形式で取得できる。
        raw_data = self.__slacker.channels.list().body

        result = []
        for data in raw_data["channels"]:
            result.append(dict(channel_id=data["id"], channel_name=data["name"]))            

        return result

    def post_message_to_channel(self, channel, message):
        """
        Slackチームの任意のチャンネルにメッセージを投稿する。
        """

        channel_name = "#" + channel
        self.__slacker.chat.post_message(channel_name, message)


slack = Slack("xoxp-8287559173-9517193584-113147450805-baefd83f3c433756418e7f31be6e7783")


while True:
    slack.post_message_to_channel("monitoring", "test")
    print("Generated at" + "2016-12-16 12:21:33.061632")
    systate = str(commands.getoutput("ps aux | grep isaax"))
    print(systate)
    print(date)
    time.sleep(30)
