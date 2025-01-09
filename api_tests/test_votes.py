import pytest
import requests

from config.config import Config
from utils.logger import logger  # Import logger


@pytest.mark.api
class TestVotes:
    VOTES_URL = f"{Config.BASE_URL}/votes"

    @pytest.fixture(scope="class")
    def headers(self):
        return {'x-api-key': Config.API_KEY, 'Content-Type': 'application/json'}

    @pytest.fixture(scope="class")
    def vote_id(self, headers):
        logger.debug("Creating a new vote for testing")
        payload = {"image_id": "asf2", "value": 1}
        response = requests.post(self.VOTES_URL, headers=headers, json=payload)
        assert response.status_code == 201, "Failed to create vote"
        vote_id = response.json().get('id')
        logger.info(f"Vote created with ID: {vote_id}")
        return vote_id

    def test_create_vote(self, headers, vote_id):
        logger.debug(f"Testing fetching of created vote with ID: {vote_id}")
        response = requests.get(f"{self.VOTES_URL}/{vote_id}", headers=headers)
        assert response.status_code == 200, "Fetching vote should respond with status code 200"
        logger.info("Create vote test passed")

    def test_get_vote(self, headers, vote_id):
        logger.debug(f"Testing retrieval of vote with ID: {vote_id}")
        response = requests.get(f"{self.VOTES_URL}/{vote_id}", headers=headers)
        assert response.status_code == 200, "Fetching vote should respond with status code 200"
        logger.info("Get vote test passed")

    def test_delete_vote(self, headers, vote_id):
        logger.debug(f"Testing deletion of vote with ID: {vote_id}")
        response = requests.delete(f"{self.VOTES_URL}/{vote_id}", headers=headers)
        assert response.status_code == 200, "Deleting vote should respond with status code 200"
        logger.info("Delete vote test passed")

    @pytest.mark.smoke
    def test_health_check_votes_endpoint(self, headers):
        logger.debug("Performing smoke test on votes endpoint")
        response = requests.get(self.VOTES_URL, headers=headers)
        assert response.status_code == 200, "Votes endpoint should be healthy"
        logger.info("Votes endpoint health check passed")
