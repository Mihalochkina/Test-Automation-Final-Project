# config.py
import os

import yaml


class Config:
    # Accurately point to the directory where this script is.
    directory_path = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(directory_path, 'secret_config.yaml')

    with open(config_path, "r") as config_file:
        secret_config = yaml.safe_load(config_file)

    # API Key and other settings
    API_KEY = secret_config.get('API_KEY')
    BASE_URL = "https://api.thecatapi.com/v1"
    REPORT_DIR = "reports/api_reports/" if secret_config.get('USE_API_DIR') else "reports/ui_reports/"
    ENVIRONMENT = secret_config.get('ENVIRONMENT', 'development')
    DEBUG = secret_config.get('DEBUG', False)
