# encoding=utf-8

from slacker import Slacker


class Serpent(object):
    def __init__(self, channel, username, slack_api_key):
        self.channel = channel
        self.username = username
        self.slacker = Slacker(slack_api_key)

    def post_message(self, message):
        message = u'```{}```'.format(message)
        return self.slacker.chat.post_message(self.channel, message, username=self.username)
