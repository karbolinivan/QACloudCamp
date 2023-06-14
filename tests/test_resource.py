import allure
import pytest

from base.api import create_resource, delete_resource, get_resource
from base.models import CreateResource, Resource
from base.response import Response
from base.assertion import assert_status_code, validate, assert_json


@allure.feature('Resource')
@allure.story('Resource API')
class TestResource:

    @pytest.mark.smoke
    @allure.title('Create resource')
    def test_create_resource(self, delete_data):
        payload = CreateResource().dict()
        response = create_resource(payload)
        result = Response(response)
        json = result.json_response()
        assert_status_code(result.status_code, 201)
        validate(json, Resource)
        assert_json(json, payload)

        delete_data(json.get('id'))

    @pytest.mark.smoke
    @allure.title('Get resource')
    def test_get_resource(self, create_and_delete_data):
        id_test = create_and_delete_data.json()['id']
        response = get_resource(id_test - 1)
        result = Response(response)
        json = result.json_response()
        assert_status_code(result.status_code, 200)
        validate(json, Resource)

    @pytest.mark.smoke
    @allure.title('Delete resource')
    def test_delete_resource(self, create_data):
        id_test = create_data.json()['id']
        response = delete_resource(id_test)
        result = Response(response)
        assert_status_code(result.status_code, 200)

    @pytest.mark.regression
    @allure.title('Create invalid resource')
    def test_create_invalid_resource(self):
        response = create_resource({})
        result = Response(response)
        assert_status_code(result.status_code, 201)

    @pytest.mark.regression
    @allure.title('Get invalid resource')
    def test_get_invalid_resource(self):
        response = get_resource(-1)
        result = Response(response)
        assert_status_code(result.status_code, 404)

    @pytest.mark.regression
    @allure.title('Delete invalid resource')
    def test_delete_invalid_resource(self):
        response = delete_resource(-1)
        result = Response(response)
        assert_status_code(result.status_code, 200)
