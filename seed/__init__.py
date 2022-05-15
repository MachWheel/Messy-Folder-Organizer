from base64 import b64encode, b64decode
from os import mkdir
from os.path import isfile

from . import config
from shared import files


def update():
    ext = _to_base64(files.EXTENSIONS)
    log = _to_base64(files.LOG_CONFIG)
    seed_file = (
        f"log_config = {log}\n" 
        f"extensions = {ext}\n"
    )
    with open(files.CONFIG_SEED, 'wt') as file:
        file.write(seed_file)


def make_config_files():
    if _exists():
        return
    try:
        mkdir(files.DIR_CONFIG)
    except FileExistsError:
        pass
    make = (
        (files.EXTENSIONS, config.extensions),
        (files.LOG_CONFIG, config.log_config)
    )
    for file in make:
        _from_base64(*file)
    while not _exists():
        continue


def _to_base64(file_name):
    with open(file_name, "rb") as file:
        data = file.read()
    b64_str = b64encode(data)
    return b64_str


def _from_base64(file_name: str, b64_data: bytes):
    with open(file_name, 'wb') as file:
        file.write(b64decode(b64_data))


def _exists():
    return isfile(files.EXTENSIONS) and \
           isfile(files.LOG_CONFIG)
