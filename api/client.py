import allure
from requests import Response
from requests import get


from common import pathjoin
from config import DOG_API_URL


class Client:
    def __init__(self, url=DOG_API_URL):
        self.api_url = url

    def get_response(self, path) -> Response:
        endpoint_url = pathjoin(self.api_url, path)
        response = get(endpoint_url)
        allure.attach(response.text, "Response", attachment_type=allure.attachment_type.JSON)

        return response







