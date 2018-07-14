import configparser
import logging
class Utils:

    def __init__(self,filename):
        self.config = configparser.ConfigParser()
        self.config.read(filename)

    def get_token(self):
        return self.config['telegram']['token']

    def  get_logger(self):
        level = getattr(
            logging,
            self.config['common']['loglevel'].upper(),
        )
        logfile = self.config['common']['logfile']
        logger = logging.getLogger('telegramm_bot')

        fh = logging.FileHandler(logfile)
        fh.setLevel(logging.ERROR)

        ch = logging.StreamHandler()
        ch.setLevel(level)
