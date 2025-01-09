import os

from config.config import Config


def pytest_sessionstart(_session):
    # Automatically create directories for reports if they don't exist
    if not os.path.exists(Config.REPORT_DIR):
        os.makedirs(Config.REPORT_DIR)
