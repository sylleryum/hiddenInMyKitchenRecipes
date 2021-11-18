import requests


def get(url):
    return requests.get(url)


def post(url, payload):
    # headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(url, data=payload)
