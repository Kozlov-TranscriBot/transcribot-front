import requests
from os import remove


def send_file(user_id: int, filename) -> str:
    with open(filename, 'rb') as file:
        url = f'http://127.0.0.1:8000?id={user_id}'
        resp = requests.post(url, files={
            'file': file
        })
        remove(filename)
        return resp.content.decode("utf-8")