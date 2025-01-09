import pytest

from ui_tests.page_objects.sign_up_page import SignUpPage  # Ensure correct import path
from utils.logger import logger  # Import logger


@pytest.fixture
def sign_up_page(page):
    logger.debug("Navigating to the sign-up page")
    sign_up = SignUpPage(page)
    sign_up.navigate_to_sign_up()
    return sign_up


@pytest.mark.ui
def test_title(sign_up_page):
    logger.debug("Testing the title of the sign-up page")
    assert sign_up_page.get_title() == "Sign Up For Free Cat Images and Breed Info"
    logger.info("Sign-up page title is correct")


@pytest.mark.ui
def test_sign_up_form_visible(sign_up_page):
    logger.debug("Testing visibility of the sign-up form")
    form = sign_up_page.page.locator("form")
    assert form.is_visible()
    logger.info("Sign-up form is visible")


@pytest.mark.ui
def test_email_input_visible(sign_up_page):
    logger.debug("Testing visibility of the email input field")
    email_input = sign_up_page.email_input()
    assert email_input.is_visible()
    logger.info("Email input field is visible")


@pytest.mark.ui
def test_sign_up_button_enabled(sign_up_page):
    logger.debug("Testing if the sign-up button is enabled")
    sign_up_button = sign_up_page.sign_up_button()
    assert sign_up_button.is_enabled()
    logger.info("Sign-up button is enabled")
