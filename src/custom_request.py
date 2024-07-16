import base64
import json
import requests


class UserContent:
    def __init__(self, user_id: int, bytes: bytearray) -> None:
        self.id = user_id
        self.content = base64.b64encode(bytes).decode('utf-8')


def send_bytearray(user_id: int, bytes: bytearray) -> str:
    resp = requests.post("http://127.0.0.1:8000", json={
        "id": user_id,
        "content": base64.b64encode(bytes).decode('utf-8')
    })
    return resp.content.decode("utf-8")