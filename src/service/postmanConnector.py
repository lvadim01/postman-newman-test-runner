import requests


class PostmanConnector(object):
    response_body = None

    def __init__(self, host_url, api_key, url_ext=""):
        r = requests.get(host_url + url_ext, headers={'X-Api-Key': api_key})
        self.response_body = r.content

    def get_response_body(self):
        return self.response_body
