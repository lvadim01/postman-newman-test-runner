import os
import shutil


class DirectoryManager(object):
    directory = None

    def __init__(self):
        self.directory = 'results/old'
        return

    def check_and_create_directory(self):
        path = 'results/'
        if os.listdir(path) != []:
            if not os.path.exists(self.directory):
                os.makedirs(self.directory)
            self.move_old_report(path)

    @staticmethod
    def move_old_report(path):
        for found_file in os.listdir(path):
            if found_file != 'old':
                src = 'results/' + found_file
                dst = 'results/old/' + found_file
                shutil.move(src, dst)
            else:
                continue
