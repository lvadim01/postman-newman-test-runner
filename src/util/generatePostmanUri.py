import configparser


class GeneratePostmanUri(object):
    collection_uri = None
    env_uri = None
    uid = None
    config = None

    def __init__(self, uid):
        self.config = configparser.ConfigParser()
        self.config.read('config/params.ini')
        self.uid = uid

    def get_collection_uri(self):
        try:
            res = self.config.get('postman-acc', 'coll_url') + self.uid
        except Exception:
            print 'Error: invalid Postman collection requested'
            exit(1)
        return res

    def get_env_uri(self):
        try:
            res = self.config.get('postman-acc', 'env_url') + self.uid
        except Exception:
            print 'Error: invalid Postman environment requested'
            exit(1)
        return res


