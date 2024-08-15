import requests
from os import remove
from telegram import File

from .misc import get_file_path

class AudioData:
    def __init__(self, lang_code: str, file: File) -> None:
        self.lang_code = lang_code
        self.file = file

    async def send(self, user_id: int) -> str:
        path = await self.file.download_to_drive(get_file_path(user_id))
        with open(path, 'rb') as file:
            url = f'http://127.0.0.1:8000?id={user_id}&lang={self.lang_code}'
            resp = requests.post(url, files={
                'file': file
            })
            remove(path)
            return resp.content.decode("utf-8")