import logging


class Logger():

    def __init__(self):
        self.FORMAT  = '%(asctime)s - %(levelname)s: %(message)s'
        self.format = logging.basicConfig(
            filename=None,
            level=logging.DEBUG,
            format=self.FORMAT)

    def logger(self, level, msg):
        level = level.upper()
        if level == 'INFO':
            logging.info(msg)
        elif level == 'DEBUG':
            logging.debug(msg)
        elif level == 'WARNING':
            logging.warning(msg)
        elif level == 'ERROR':
            logging.error(msg)
        elif level == 'CRITICAL':
            logging.critical(msg)
        else:
            raise ValueError('Unknown log level %s, available: INFO, WARNING, DEBUG, ERROR, CRITICAL' % msg)

if __name__ == '__main__':
    l = Logger()
    lev = ['INFO', 'warning', 'Debug', 'ERROR', 'CRITICAL']
    for i in lev:
        l.logger(i, i)
