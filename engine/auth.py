import json

CONFIG_PATH = 'tasks/config.json'


def save_auth_token(token):
    with open(CONFIG_PATH) as f:
        config = json.load(f)

    config['authToken'] = token

    with open(CONFIG_PATH, 'w') as f:
        f.writelines(json.dumps(config, sort_keys=True, indent=2, separators=(',', ': ')))
