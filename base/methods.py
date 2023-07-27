import allure
import requests
from utils.logger import logs


class Requests:

    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}

    @allure.step("GET request to {url}")
    def get(self, url):
        logs.save_request(method="GET", url=url)
        result = requests.get(url=url)
        logs.save_response(response=result)
        return result

    @allure.step("POST request to {url}")
    def post(self, url, body):
        logs.save_request(method="POST", url=url, json=body, headers=self.headers)
        result = requests.post(url=url, json=body, headers=self.headers)
        logs.save_response(response=result)
        return result

    @allure.step("DELETE request to {url}")
    def delete(self, url):
        logs.save_request(method="DELETE", url=url)
        result = requests.delete(url=url)
        logs.save_response(response=result)
        return result
