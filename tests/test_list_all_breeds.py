import allure
from api.endpoint import Endpoint


@allure.epic("Epic")
@allure.feature("Feature")
def test_list_all_breeds():
    endpoint = Endpoint(scale="breeds", quantity="all", representation="list")
    endpoint.list_all_breeds()
