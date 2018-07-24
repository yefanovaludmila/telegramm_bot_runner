from telepot.namedtuple import ReplyKeyboardMarkup
import time

class View:
    d_stop = {}
    d_start = {}
    d_circle = []
    d_runner = []
    markup = ReplyKeyboardMarkup(keyboard=[['Start', 'Circle'], ['Stop']])
    def __init__(self, bot):
        self.bot = bot

    def nul_values(self):
        self.d_stop = {}
        self.d_start = {}
        self.d_circle = []

    def start_stop_run(self, text, date):
        d_start_stop = {text: date}
        return d_start_stop

    def unresolved_choice(self, msg):
        self.bot.sendMessage(msg['chat']['id'], msg['chat']['first_name'] + ', please choose button Start or Stop',
                             reply_markup=self.markup)

    def text_start(self, txt, date):
        self.d_start = View.start_stop_run(self, txt, date)
        self.d_circle = []
        self.d_circle.append(date)

    def text_circle(self, txt, date, chat_id):
        if (self.d_start.get("Start", 0) > 0):
            self.d_circle.append(date)
        else:
            self.bot.sendMessage(chat_id, f"first press the \'Start\' button", reply_markup=self.markup)

    def text_stop(self, txt, date, first_name):
        self.d_stop = View.start_stop_run(self, txt, date)
        self.d_circle.append(date)
        self.d_runner.append([self.d_start, {"Circle": self.d_circle}, self.d_stop, {"Run_time":self.d_stop.get("Stop", 0) - self.d_start.get("Start", 0)}, {"User": first_name}])
        print(self.d_runner)

    def date_format(self, date):
        new_date = time.strftime('%H:%M:%S', time.gmtime(date))
        return new_date

    def get_value_runner(self, value, i):
        if i == 0:
            lst = []
            for keys in self.d_runner:
                for k in keys:
                    for i, j in k.items():
                        if i == value:
                            lst.append(j)
            return lst
        else:
            for k in self.d_runner[-i]:
                for i, j in k.items():
                    if i == value:
                        return j

    def circle_time(self, chat_id):
        j = View.get_value_runner(self, 'Circle', 1)
        for ind, value  in enumerate(j[1::]):
            self.bot.sendMessage(chat_id, f'{ind+1} circle: {View.date_format(self, value - j[ind])}')

    def best_time(self, run_time, chat_id):
        if run_time[-1] == min(run_time):
            self.bot.sendMessage(chat_id, 'It\'s your best time! Congrats!!!')
        else:
            return


    def calculate_run_time(self, chat_id):
        if (self.d_start.get("Start", 0) > 0):
            run_time = View.get_value_runner(self, 'Run_time', 0)
            print(run_time)
            self.bot.sendMessage(chat_id, f'Run time is: {View.date_format(self, run_time[-1])}', reply_markup=self.markup)
            View.best_time(self, run_time, chat_id)
            self.bot.sendMessage(chat_id, f'Count of circles: {len(self.d_circle)-1}')
            View.nul_values(self)
        else:
            self.bot.sendMessage(chat_id, f"first press the \'Start\' button", reply_markup=self.markup)

    def test_type(self, msg):
        try:
            txt = msg['text']
        except KeyError as error:
            self.bot.sendMessage(msg['chat']['id'], 'Choose the button')
            return error

    def root_handle(self, msg):
        print(msg)
        View.test_type(self, msg)
        if (msg['text'] == "Start"):
            View.text_start(self,msg['text'], msg['date'])
        elif (msg['text'] == "Circle"):
            View.text_circle(self, msg['text'], msg['date'], msg['chat']['id'])
        elif (msg['text'] == "Stop"):
            View.text_stop(self, msg['text'], msg['date'], msg['chat']['first_name'])
            View.calculate_run_time(self, msg['chat']['id'])
            View.circle_time(self,msg['chat']['id'])
        else:
            View.unresolved_choice(self, msg)















