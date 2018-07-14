from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
import telepot
import datetime
import time

class View:
    d = {}
    def __init__(self,bot):
        self.bot = bot

    def root_handle(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        markup = ReplyKeyboardMarkup(keyboard=[['Start', 'Stop']])
        if (msg['text'] == "Start" or msg['text'] == "Stop"):

            self.bot.sendMessage(chat_id, f"{msg['text']} time is "
                                     f"{datetime.datetime.fromtimestamp(msg['date']).strftime('%Y-%m-%d %H:%M:%S')}",
                            reply_markup=markup)
            self.d[msg['text']] = msg['date']
        else:
            self.bot.sendMessage(chat_id, msg['chat']['first_name'] + ', please choose button Start or Stop', reply_markup=markup)
        if (msg['text'] == "Stop"):
            run_time = self.d.get("Stop", 0) - self.d.get("Start", 0)
            new_run_time = time.strftime('%H:%M:%S', time.gmtime(run_time))
            srt_run_time = msg['chat'][
                               'first_name'] + f', your run time is {new_run_time}. You are the best runner in the world!!!'
            self.bot.sendMessage(chat_id, srt_run_time, reply_markup=markup)
        