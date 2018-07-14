from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
import time

class View:
    d_stop = {}
    d_start ={}
    d_circle = []
    d_runner = []
    def __init__(self,bot):
        self.bot = bot

    def start_stop_run(self, text, date):
        d_start_stop = {text: date}
        return d_start_stop

    def unresolved_choice(self, msg):
        markup = ReplyKeyboardMarkup(keyboard=[['Start', 'Circle'], ['Stop']])
        self.bot.sendMessage(msg['chat']['id'], msg['chat']['first_name'] + ', please choose button Start or Stop',
                             reply_markup=markup)

    def root_handle(self,msg):
        print(msg['date'])
        markup = ReplyKeyboardMarkup(keyboard=[['Start', 'Circle'], ['Stop']])
        if (msg['text'] == "Start"):
            self.d_start = View.start_stop_run(self,msg['text'], msg['date'])
        elif (msg['text'] == "Circle"):
            if (self.d_start.get("Start", 0) > 0):
                run_circle = View.start_stop_run(self, msg['text'], msg['date'])
                self.d_circle.append(run_circle)
            else:
                self.bot.sendMessage(msg['chat']['id'], f"first press the \'Start\' button",reply_markup=markup)
        elif (msg['text'] == "Stop"):
            self.d_stop = View.start_stop_run(self, msg['text'], msg['date'])
            self.d_runner.append([{"Start":self.d_start},{"Circle":self.d_circle},{"Stop":self.d_stop},{"User":msg['chat']['first_name']}])
            if(self.d_start.get("Start", 0)>0):
                run_time = self.d_stop.get("Stop", 0) - self.d_start.get("Start", 0)
                new_run_time = time.strftime('%H:%M:%S', time.gmtime(run_time))
                self.bot.sendMessage(msg['chat']['id'], f'run time is: {new_run_time}', reply_markup=markup)

                self.bot.sendMessage(msg['chat']['id'],f'count of circles: {len(self.d_circle)+1}')
                self.d_stop = {}
                self.d_start = {}
                self.d_circle = []
            else:
                self.bot.sendMessage(msg['chat']['id'], f"first press the \'Start\' button",reply_markup=markup)
        else:
            View.unresolved_choice(msg)















