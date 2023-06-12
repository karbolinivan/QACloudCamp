import pytest

from base.api import create_resource, delete_resource
from base.models import CreateResource


@pytest.fixture(scope='function')
def create_data():
    resource = create_resource(CreateResource().dict())
    return resource


def _delete_data(id_resource=None):
    return delete_resource(id_resource)


@pytest.fixture(scope='function')
def delete_data():
    yield _delete_data


@pytest.fixture(scope='function')
def create_and_delete_data():
    resource = create_resource(CreateResource().dict())
    yield resource
    delete_resource(resource.json()['id'])
