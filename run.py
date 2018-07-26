import time
import argparse
import logging

import telepot
from telepot.loop import MessageLoop
from utils import Utils
from view import View


def setup_logger(logfile, level):
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(logfile)
    fh.setLevel(logging.ERROR)

    ch = logging.StreamHandler()
    ch.setLevel(level)



parser = argparse.ArgumentParser(description='Some initial bot.')
parser.add_argument('--config', type=str,
                    help='A config fole with required params',
                    required=True)
args = parser.parse_args()

logger = logging.getLogger('telegramm_bot')

uti = Utils(args.config)
TOKEN = uti.get_token()

bot = telepot.Bot(TOKEN)
viwer = View(bot)


def main():
    MessageLoop(bot, viwer.root_handle).run_as_thread()
    # import logging
    print('I am ready to work ...')

while 1:
    time.sleep(10)
