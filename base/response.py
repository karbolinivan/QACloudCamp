
class Response:

    def __init__(self, response):
        self.response = response
        self.status_code = response.status_code

    def json_response(self):
        return self.response.json()
