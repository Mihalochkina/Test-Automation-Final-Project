import pytest

from ui_tests.page_objects.home_page import HomePage
from utils.logger import logger  # Import logger


@pytest.mark.ui
def test_home_page_load(page):
    logger.debug("Testing home page load")
    home_page = HomePage(page)
    home_page.navigate_to_home()
    assert home_page.get_title() == "The Cat API - Cat as a Service"
    logger.info("Home page loaded successfully with correct title")


@pytest.mark.ui
def test_get_started_button_visible(page):
    logger.debug("Testing visibility of the 'Get Started' button on the home page")
    home_page = HomePage(page)
    home_page.navigate_to_home()
    button = home_page.get_started_button()
    assert button.is_visible()
    logger.info("'Get Started' button is visible on the home page")


@pytest.mark.ui
def test_navigation_to_sign_up(page):
    logger.debug("Testing navigation to the sign-up page via 'Get Started' button")
    home_page = HomePage(page)
    home_page.navigate_to_home()
    button = home_page.get_started_button()
    with page.expect_navigation():
        button.click()
    assert page.url == 'https://thecatapi.com/signup'
    logger.info("Successfully navigated to the sign-up page")
