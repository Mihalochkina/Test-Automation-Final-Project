import pytest
import requests

from config.config import Config
from utils.logger import logger  # Import logger


@pytest.mark.api
class TestImages:
    IMAGES_URL = f"{Config.BASE_URL}/images"

    @pytest.fixture(scope="class")
    def headers(self):
        return {'x-api-key': Config.API_KEY}

    def test_fetch_random_image(self, headers):
        logger.debug("Testing fetching of a random image")
        response = requests.get(f"{self.IMAGES_URL}/search", headers=headers)
        assert response.status_code == 200, "Response status code should be 200"
        assert 'application/json' in response.headers['Content-Type'], "Content-Type should be application/json"
        data = response.json()
        assert len(data) > 0, "No images were returned"
        logger.info("Random image fetch test passed")

    def test_specific_image_search(self, headers):
        logger.debug("Testing specific image search with criteria")
        params = {'limit': 3, 'page': 1, 'order': 'ASC'}
        response = requests.get(f"{self.IMAGES_URL}/search", headers=headers, params=params)
        assert response.status_code == 200, "Response status code should be 200"
        data = response.json()
        assert len(data) == 3, "Number of images returned should be 3"
        logger.info("Specific image search test passed")

    def test_image_content_type(self, headers):
        logger.debug("Testing images endpoint for correct content type")
        response = requests.get(f"{self.IMAGES_URL}/search", headers=headers)
        assert 'application/json' in response.headers['Content-Type'], "Content type should be application/json"
        logger.info("Image content type test passed")

    @pytest.mark.smoke
    def test_health_check_images_endpoint(self, headers):
        logger.debug("Performing smoke test on images endpoint")
        response = requests.get(f"{self.IMAGES_URL}/search", headers=headers)
        assert response.ok, "The images endpoint is not healthy"
        logger.info("Images endpoint health check passed")
