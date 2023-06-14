import logging
import allure

from utils.constants import BASE_URL
from base.methods import Requests

logger = logging.getLogger("api")


@allure.step('Get a resource with id "{id_resource}"')
def get_resource(id_resource):
    url = f'{BASE_URL}/{id_resource}'
    result = Requests().get(url)
    logger.info(f'\nGetting a resource'
                f'\nStatus code: {result.status_code}')
    return result


@allure.step('Create a resource')
def create_resource(body):
    url = BASE_URL
    result = Requests().post(url, body)
    logger.info(f'\nCreating a resource'
                f'\nStatus code: {result.status_code}'
                f'\nStatus code: {result.text}')
    return result


@allure.step('Delete a resource with id "{id_resource}"')
def delete_resource(id_resource):
    url = f'{BASE_URL}/{id_resource}'
    result = Requests().delete(url)
    logger.info(f'\nDeleting a resource'
                f'\nStatus code: {result.status_code}')
    return result
