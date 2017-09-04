import argparse


class ArgumentParser(object):
    parser = None
    arguments = None

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.add_arguments()

    def add_arguments(self):
        self.parser.add_argument('-e', action='store', dest='environment', default='test',
                                 help='Postman environment')
        self.parser.add_argument('-c', action='store', dest='collection', default='[test_coll]',
                                 help='Postman collection [hr,sfc]')
        self.parser.add_argument('-r', action='store', dest='report', default='false', type=str,
                                 help='Send email report true/false')
        self.arguments = self.parser.parse_args()

        return

    def get_arguments(self):
        return self.arguments
