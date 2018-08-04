import time
import argparse
import logging

import telepot
from telepot.loop import MessageLoop
# from utils import Utils
from view import View
from flask import Flask
app = Flask(__name__)

# def setup_logger(logfile, level):
#     logger.setLevel(logging.DEBUG)
#
#     fh = logging.FileHandler(logfile)
#     fh.setLevel(logging.ERROR)
#
#     ch = logging.StreamHandler()
#     ch.setLevel(level)
#
# parser = argparse.ArgumentParser(description='Some initial bot.')
# parser.add_argument('--config',
#                     type=str,
#                     help='A config fole with required params',
#                     required=True)
# args = parser.parse_args()
#
# logger = logging.getLogger('telegramm_bot')

# uti = Utils(args.config)
# TOKEN = uti.get_token()
TOKEN = 'AAFUiHtSM8Y7nkpSflHzfT9zPvpPxrk5jwk'
bot = telepot.Bot(TOKEN)
viwer = View(bot)

MessageLoop(bot, viwer.root_handle).run_as_thread()
print('I am ready to work ...')

# while 1:
#     time.sleep(10)
if __name__ == '__main__':
    app.run()
