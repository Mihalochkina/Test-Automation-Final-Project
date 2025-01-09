import pytest

from ui_tests.page_objects.documentation_page import DocumentationPage
from utils.logger import logger  # Import logger


@pytest.mark.ui
def test_documentation_page_load(page):
    logger.debug("Testing documentation page load")
    doc_page = DocumentationPage(page)
    doc_page.navigate_to_documentation()
    assert doc_page.get_title() == "Report - 🖼️ Basics: Getting Images"
    logger.info("Documentation page loaded successfully with correct title")


@pytest.mark.ui
def test_header_visible(page):
    logger.debug("Testing visibility of the header on the documentation page")
    page.goto("https://docs.thecatapi.com")
    header = page.locator("header")
    assert header.is_visible(), "Header should be visible on the page"
    logger.info("Header is visible on the documentation page")


@pytest.mark.ui
def test_navigation_to_example(page):
    logger.debug("Testing navigation to the '💻 Code Samples' section")
    page.goto("https://docs.thecatapi.com")
    example_link = page.locator("text='💻 Code Samples'")
    assert example_link.is_visible(), "The link to the Code Samples should be visible."
    with page.expect_navigation():
        example_link.click()
    assert page.title() == "Report - 💻 Code Samples"
    logger.info("Navigated to Code Samples section successfully")
