from enum import Enum


class Error(Enum):
    WRONG_STATUS_CODE = 'Status code is different than expected'
    WRONG_VALUE_KEY = 'Invalid key value'
