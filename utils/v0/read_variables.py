import os
import json

def get_configs_secretes(CURRENT_ENV):
    CONF_FOLDER = 'settings/conf/{0}'.format(CURRENT_ENV)
    SECRET_CONFIG_PATH_CONFIGS = os.path.join(os.getcwd(), CONF_FOLDER, 'configs.json')
    SECRET_CONFIG_PATH_SECRETES = os.path.join(os.getcwd(), CONF_FOLDER, 'secretes.json')
    SECRET_CONFIG_PATH_GOOGLE = os.path.join(os.getcwd(), CONF_FOLDER, 'client_secret_google_login.json')
    SECRET_CONFIG_PATH_FB = os.path.join(os.getcwd(), CONF_FOLDER, 'client_secret_google_login.json')
    with open(SECRET_CONFIG_PATH_CONFIGS, 'rb') as f:
        configs = f.read()
        configs = json.loads(configs)
    with open(SECRET_CONFIG_PATH_SECRETES, 'rb') as f:
        secretes = f.read()
        secretes = json.loads(secretes)
    print(configs, secretes, type(configs), type(secretes))
    return configs, secretes
