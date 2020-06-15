import inspect
import logging


class BaseClass:
    def getblogger(self):
        logname = inspect.stack()[1][3]
        log = logging.getLogger(logname)
        fh = logging.FileHandler('logtest1.log')
        formatting = logging.Formatter(" %(asctime)s :%(levelname)s : %(name)s : %(message)s :")
        fh.setFormatter(formatting)
        log.addHandler(fh)

        log.setLevel(logging.DEBUG)
        return log
