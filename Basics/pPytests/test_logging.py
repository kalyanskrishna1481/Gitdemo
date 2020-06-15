import inspect
import logging


def test_log():
    logname = inspect.stack()[1][3]
    log = logging.getLogger(__name__)
    fh = logging.FileHandler('logtest.log')
    formatting = logging.Formatter(" %(asctime)s :%(levelname)s : %(name)s : %(message)s :")
    fh.setFormatter(formatting)
    log.addHandler(fh)

    log.setLevel(logging.WARNING)

    log.debug("A debug statement")
    log.info("an info statement")
    log.warning(" a warning statement")
    log.error("an error statement")
    log.critical("a critical statement")
