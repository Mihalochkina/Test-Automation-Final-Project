import pytest
import requests

from config.config import Config
from utils.logger import logger  # Import logger


@pytest.mark.api
class TestBreeds:
    BREEDS_URL = f"{Config.BASE_URL}/breeds"

    @pytest.fixture(scope="class")
    def headers(self):
        return {'x-api-key': Config.API_KEY}

    def test_breeds_status_code(self, headers):
        logger.debug("Testing breeds endpoint for correct status code")
        response = requests.get(self.BREEDS_URL, headers=headers)
        assert response.status_code == 200, "Response status code should be 200"
        logger.info(f"Breeds status code test passed with status {response.status_code}")

    def test_breeds_content_type(self, headers):
        logger.debug("Testing breeds endpoint for correct content type")
        response = requests.get(self.BREEDS_URL, headers=headers)
        assert 'application/json' in response.headers['Content-Type'], "Content-Type should be application/json"
        logger.info("Breeds content type test passed")

    def test_specific_breed(self, headers):
        breed_code = 'abys'
        logger.debug(f"Testing retrieval of specific breed: {breed_code}")
        response = requests.get(f"{self.BREEDS_URL}/{breed_code}", headers=headers)
        assert response.status_code == 200, "Response status code should be 200"
        assert response.json()['id'] == breed_code, f"No breed found with code {breed_code}"
        logger.info(f"Specific breed test passed for breed code: {breed_code}")

    def test_search_breeds_with_query_and_image_attached(self, headers):
        query = 'air'
        logger.debug(f"Testing breed search with query '{query}' and image attached")
        response = requests.get(f"{self.BREEDS_URL}/search?q={query}&attach_breed=0&attach_image=1", headers=headers)
        assert response.status_code == 200, "Response status code should be 200"
        data = response.json()
        assert len(data) > 0, "Search should return results"
        assert 'image' in data[0], "Returned data should include an image"
        logger.info("Breed search with query and image test passed")

    def test_list_all_breeds(self, headers):
        logger.debug("Testing retrieval of all breeds")
        response = requests.get(self.BREEDS_URL, headers=headers)
        assert response.status_code == 200, "Response status code should be 200"
        data = response.json()
        assert len(data) > 0, "Breed list should not be empty"
        logger.info("List all breeds test passed")

    @pytest.mark.smoke
    def test_health_check_breeds_endpoint(self, headers):
        logger.debug("Performing smoke test on breeds endpoint")
        response = requests.get(self.BREEDS_URL, headers=headers)
        assert response.ok, "Breeds endpoint is not healthy"
        logger.info("Breeds endpoint health check passed")
