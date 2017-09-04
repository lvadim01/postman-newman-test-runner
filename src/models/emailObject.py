import configparser


class EmailObject(object):
    config = None
    send_from = None
    send_to = []
    subject = None
    text = None
    files = []
    server = None

    def __init__(self, files, env, collection):
        self.config = configparser.ConfigParser()
        self.config.read('config/params.ini')

        self.set_sender()
        self.set_recipient()
        self.set_subject(env)
        self.set_body()
        self.set_server()
        self.set_file(files)

    def set_sender(self):
        self.send_from = self.config.get('gmail-account', 'user_name')

    def set_recipient(self):
        self.send_to = self.config.get('gmail-account', 'send_email_to').split()

    def set_subject(self, env):
        env_title = env.title()
        self.subject = '[ ' + env_title + ' ]' + ' API test run report'

    def set_body(self):
        self.text = 'Greetings! \n \
                     Please find attached the report file. '

    def set_server(self):
        gmail_server = self.config.get('gmail-account', 'gmail_server')
        gmail_port = self.config.get('gmail-account', 'gmail_port')
        self.server = gmail_server + ':' + gmail_port

    def set_file(self, files):
        self.files = files

    def get_sender(self):
        return self.send_from

    def get_recipient(self):
        return self.send_to

    def get_subject(self):
        return self.subject

    def get_body(self):
        return self.text

    def get_server(self):
        return self.server

    def get_files(self):
        return self.files
