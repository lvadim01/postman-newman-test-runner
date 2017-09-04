import os
import configparser
from models.outputFile import OutputFile
from service.postmanLoader import PostmanLoader
from util.generateNewmanCmd import GenerateNewmanCmd
from util.generatePostmanUri import GeneratePostmanUri
from service.directoryManager import DirectoryManager


class RunTests(object):
    env = None
    collections = []

    def __init__(self, env, collections):
        config = configparser.ConfigParser()
        config.read('config/params.ini')
        self.set_envs_to_run(config, collections)
        self.env = config.get('environment', env)

    def filter_postman_response(self, items, filter):
        res = None
        for item in items:
            tmp = item.get_name()
            if filter == tmp:
                res = item.get_id()
            else:
                continue

        return res

    def set_envs_to_run(self, config, collections):
        for name in collections:
            param = config.get('component', name)
            self.collections.append(param)

    def run_tests(self):

        file_name_list = []
        try:
            loader = PostmanLoader()
            environments = loader.get_all_envs()
            collections = loader.get_all_collections()
        except Exception:
            print 'Error: Cannot query Postman API Library!'
            exit(1)

        try:
            directory = DirectoryManager()
            directory.check_and_create_directory()
        except Exception:
            print 'Error: Cannot read/write directories!'
            exit(1)

        for collection_item in self.collections:
            coll_id = self.filter_postman_response(collections, collection_item)
            coll_uri_generator = GeneratePostmanUri(coll_id)

            env_id = self.filter_postman_response(environments, self.env)
            env_uri_generator = GeneratePostmanUri(env_id)

            collection_uri = coll_uri_generator.get_collection_uri()
            env_uri = env_uri_generator.get_env_uri()

            try:
                newman_cmd_generator = GenerateNewmanCmd(collection_uri, env_uri)
                result_file = OutputFile(collection_item)
                file_name_list.append(result_file.get_filename())
                newman_cmd = newman_cmd_generator.get_newman_run_cmd_html_report(result_file.get_filename())
                os.system(newman_cmd)
            except Exception:
                print 'Error: Cannot run Newman commands'
                exit(1)

        return file_name_list

