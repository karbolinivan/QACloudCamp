import allure
import requests


class Requests:

    def __init__(self, headers=None):
        self.headers = {'Content-Type': 'application/json'}

    @allure.step("POST request to {url}")
    def get(self, url):
        return requests.get(url=url)

    @allure.step("POST request to {url}")
    def post(self, url, body):
        return requests.post(url=url, json=body, headers=self.headers)

    @allure.step("DELETE request to {url}")
    def delete(self, url):
        return requests.delete(url=url)
