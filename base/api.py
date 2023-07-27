import allure

from utils.constants import BASE_URL
from base.methods import Requests


@allure.step('Get a resource with id "{id_resource}"')
def get_resource(id_resource):
    url = f'{BASE_URL}/{id_resource}'
    result = Requests().get(url)
    return result


@allure.step('Create a resource')
def create_resource(body):
    url = BASE_URL
    result = Requests().post(url, body)
    return result


@allure.step('Delete a resource with id "{id_resource}"')
def delete_resource(id_resource):
    url = f'{BASE_URL}/{id_resource}'
    result = Requests().delete(url)
    return result
