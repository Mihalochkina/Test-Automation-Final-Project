import pytest
from requests import Session
from config.config import Config
from utils.logger import logger  # Directly use logger from logger.py

# Fixture to handle API session setup and teardown
@pytest.fixture(scope="session")
def api_client():
    session = Session()
    session.headers.update({'x-api-key': Config.API_KEY})
    yield session
    session.close()

# Fixture to manage custom logger
@pytest.fixture(scope="session")
def setup_logger():
    return logger

# Pytest hook to log exceptions globally
def pytest_exception_interact(node, call, report):
    if report.failed:
        # Log the exception with traceback
        logger.exception(f"Exception in {node.nodeid}: {call.excinfo.typename}, {call.excinfo.value}")