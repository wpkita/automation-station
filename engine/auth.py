from engine import config


def set_auth_token(token):
    config.set_value('authToken', token)
