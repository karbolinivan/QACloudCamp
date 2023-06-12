import allure
from utils.enums import Error
from pydantic import ValidationError


@allure.step('Assert status code')
def assert_status_code(status_code, expect):
    assert status_code == expect, Error.WRONG_STATUS_CODE.value


@allure.step('Validating schema')
def validate(json, schema):
    try:
        schema.parse_obj(json)
    except ValidationError as e:
        raise AttributeError(f"Could not map received object to pydantic schema:\n{e.json()}")


@allure.step('Assert key value')
def assert_json(json, expect):
    for item in expect:
        assert expect.get(item) == json.get(item), Error.WRONG_VALUE_KEY.value
