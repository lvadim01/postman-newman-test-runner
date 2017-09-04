import configparser


class GenerateNewmanCmd(object):
    collection_uri = None
    env_uri = None
    api_key = None

    def __init__(self, collUri, envUri):
        config = configparser.ConfigParser()
        config.read('config/params.ini')
        self.api_key = config.get('postman-acc', 'api_key')

        self.collection_uri = collUri
        self.env_uri = envUri

    def get_newman_run_cmd(self):
        res = 'newman run --url ' + self.collection_uri + '?apikey=' + self.api_key + \
              ' --environment-url ' + self.env_uri + '?apikey=' + self.api_key
        return res

    def get_newman_run_cmd_html_report(self, outputFile):
        res = 'newman run --url ' + self.collection_uri + '?apikey=' + self.api_key + \
              ' --environment-url ' + self.env_uri + '?apikey=' + self.api_key + \
              ' --html ' + outputFile
        return res
