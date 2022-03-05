# coding=utf-8
import json
from os import mkdir

import PySimpleGUI as sg

from .logger import Log
from .names import mes_ano
from .messages import APP_TITLE, CANCELLED, SELECT_FOLDER


def get_working_folder() -> str:
    working_folder = sg.Window(
        APP_TITLE,
        [
            [sg.Text(SELECT_FOLDER)],
            [sg.In(), sg.FolderBrowse()],
            [sg.Open(), sg.Cancel()]
        ]
    ).read(close=True)[1][0]
    if not working_folder:
        sg.popup(CANCELLED)
        raise SystemExit(CANCELLED)
    return working_folder


def make_destination_folder(working_folder) -> tuple[str, bool]:
    dest_folder = f"{working_folder}/{mes_ano()}"
    try:
        mkdir(dest_folder)
        created = True
    except FileExistsError:
        created = False
    return dest_folder, created


def get_extensions() -> dict[str, list[str]]:
    with open("app/extensions.json", "r") as extensions_file:
        return json.load(extensions_file)


def get_category_name(file_extension) -> str:
    extensions = get_extensions()
    for category, entries in extensions.items():
        if file_extension in entries:
            folder_name = category.capitalize()
            return folder_name
    return "Arquivos"


def make_category_folder(destination_folder, category_name) -> str:
    category_folder = f"{destination_folder}/{category_name}"
    try:
        mkdir(category_folder)
    except FileExistsError:
        pass
    return category_folder
