from api.client import Client
from config import STATUS_CODE_SUCCESS
from common import pathjoin


class Endpoint:
    def __init__(
            self,
            scale: str,
            breed: str = None,
            sub_breed: str = None,
            randomization: str = None,
            representation: str = None,
            image: str = None,
            quantity: str = None,
            expected_status_code: int = STATUS_CODE_SUCCESS
            ):
        self.api_client = Client()
        self.scale = scale
        self.breed = breed
        self.sub_breed = sub_breed
        self.randomization = randomization
        self.representation = representation
        self.image = image
        self.quantity = quantity
        self.expected_status_code = expected_status_code

    def list_all_breeds(self):
        path = pathjoin(self.scale, self.representation, self.quantity)
        resp = self.api_client.get_response(path)
        assert resp.status_code == self.expected_status_code, resp.json()




