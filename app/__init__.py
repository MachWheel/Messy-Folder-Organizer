# coding=utf-8
from .names import mes_ano
from .logger import Logger
from os import mkdir
import PySimpleGUI as sg
import json


def get_working_folder() -> str:
    working_folder = sg.Window(
        'Organizador',
        [
            [sg.Text('Selecione uma pasta para organizar: ')],
            [sg.In(), sg.FolderBrowse()],
            [sg.Open(), sg.Cancel()]
        ]
    ).read(close=True)[1][0]
    if not working_folder:
        sg.popup("Cancelado", "Nenhuma pasta escolhida")
        raise SystemExit("Cancelando, nenhuma pasta escolhida.")
    return working_folder


def make_destination_folder(working_folder) -> str:
    dest_folder = f"{working_folder}/{mes_ano()}"
    msgs = Logger(working_folder)
    try:
        mkdir(dest_folder)
        msgs.log(f"Pasta '{dest_folder}' criada.\n"
                 f"Movendo arquivos para ela...")
    except FileExistsError:
        msgs.log(f"Movendo arquivos para '{dest_folder}'...")
    return dest_folder


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
