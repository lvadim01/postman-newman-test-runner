import datetime
import random


class OutputFile(object):

    def __init__(self, report_name):
        datetime_suffix = datetime.datetime.now().strftime('%Y-%m-%d')
        default_file_name = 'results/' + report_name
        self.name = default_file_name + '_' + str(datetime_suffix) + '_' + str(random.randrange(99)) + '.html'

    def get_filename(self):
        return self.name
