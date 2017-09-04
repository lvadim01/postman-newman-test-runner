import json
import configparser
from models.testCollection import TestCollection
from models.testEnvironment import TestEnvironment
from service.postmanConnector import PostmanConnector


class PostmanLoader(object):
    host_url = None
    api_key = None

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config/params.ini')
        self.host_url = config.get('postman-acc', 'host')
        self.api_key = config.get('postman-acc', 'api_key')

    def get_collection(self, collection_id):
        connector = PostmanConnector(self.host_url, self.api_key, 'collections/' + collection_id)
        res = connector.get_response_body()
        return res

    def get_environment(self, env_id):
        connector = PostmanConnector(self.host_url, self.api_key, 'environments/' + env_id)
        res = connector.get_response_body()
        return res

    def get_all_collections(self):
        connector = PostmanConnector(self.host_url, self.api_key, 'collections')
        res = connector.get_response_body()
        json_res = json.loads(res)

        collection_list = []

        for item in json_res['collections']:
            collection = TestCollection(item['name'], item['uid'])
            collection_list.append(collection)

        return collection_list

    def get_all_envs(self):
        connector = PostmanConnector(self.host_url, self.api_key, 'environments')
        res = connector.get_response_body()
        json_res = json.loads(res)

        env_list = []

        for item in json_res['environments']:
            environment = TestEnvironment(item['name'], item['uid'])
            env_list.append(environment)

        return env_list