import logging
import allure

from utils.constants import BASE_URL
from base.methods import Requests

logger = logging.getLogger("api")


@allure.step('Getting resource with id "{id_resource}"')
def get_resource(id_resource):
    url = f'{BASE_URL}/{id_resource}'
    result = Requests().get(url)
    logger.info(f'\nGetting resource'
                f'\nStatus code: {result.status_code}')
    return result


@allure.step('Create resource')
def create_resource(body):
    url = BASE_URL
    result = Requests().post(url, body)
    logger.info(f'\nCreating resource'
                f'\nStatus code: {result.status_code}'
                f'\nStatus code: {result.text}')
    return result


@allure.step('Delete resource with id "{id_resource}"')
def delete_resource(id_resource):
    url = f'{BASE_URL}/{id_resource}'
    result = Requests().delete(url)
    logger.info(f'\nDeleting resource'
                f'\nStatus code: {result.status_code}')
    return result
