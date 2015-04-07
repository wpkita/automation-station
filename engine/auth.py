from engine.config import *
from httplib2 import Http


class Authorizer:
    def __init__(self):
        self.accountUri = 'https://api.dropbox.com/1/account/info'
        self.authorizationUri = 'https://www.dropbox.com/1/oauth2/authorize'
        self.local_config = LocalConfig()
        self.cloud_config = CloudConfig(self.local_config.get_task_directory())

    def is_authorized(self):
        auth_token = self.get_auth_token()

        if auth_token == '':
            return False

        # Make web request to get user's dropbox info, thereby testing the auth token
        h = Http()
        response, content = h.request(self.accountUri, headers={'Authorization': 'Bearer {0}'.format(auth_token)})

        if not response['status'] == '200':
            return False

        return True

    def get_auth_uri(self):
        dropbox_config = {
            'client_id': 'ax0k4eseumuduy8',
            'response_type': 'token',
            'redirect_uri': 'http://localhost:5000'
        }

        dropbox_auth_uri = self.authorizationUri + '?client_id={0}&response_type={1}&redirect_uri={2}'\
            .format(dropbox_config['client_id'], dropbox_config['response_type'], dropbox_config['redirect_uri'])

        return dropbox_auth_uri

    def get_auth_token(self):
        return self.cloud_config.get_value('authToken')

    def set_auth_token(self, token):
        self.cloud_config.set_value('authToken', token)
