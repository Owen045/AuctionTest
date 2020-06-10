import logging
import datetime


class Logger:
    def __init__(self, id=None):
        assert id is not None, 'Must provide with an id'
        self.id = id
        self.now = datetime.datetime.now().strftime("%d_%m_%Y %H_%M_%S")

        self.name = f'{id}_{self.now}.log'

        try:
            self.file = open(f'{self.name}', 'r')
        except FileNotFoundError:
            self.file = open(f'{self.name}', 'w')

    def init_logfile(self):
        """
        initialise logfile params
        """
        self.my_logger = logging.getLogger(self.name)
        file_handler = logging.FileHandler(fr'{self.name}', 'w')

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname(s) - %(message)s')

        file_handler.setFormatter(formatter)
        self.my_logger.addHandler(file_handler)
        self.my_logger.setLevel(logging.DEBUG)

    def add_log_row(self, message, log_level='info'):
        """
        Add new line to log file
        :return:
        """
        if log_level == 'info': # for normal bid transactions
            self.my_logger.info(message)
        elif log_level == 'error': # for error bids e.g. negatives
            self.my_logger.error(message)
        elif log_level == 'warning': # for winning bids
            self.my_logger.warning(message)