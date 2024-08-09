from pathlib import Path

PATH_PREFIX = '/tmp/transcribot-front'


def create_dir():
    path = Path(PATH_PREFIX)
    path.mkdir(exist_ok=True)


def get_file_path(filename):
    return f'{PATH_PREFIX}/{filename}'