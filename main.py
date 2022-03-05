# coding=utf-8
import os
import shutil
import PySimpleGUI as sg
import sys
from app import get_working_folder, make_destination_folder, get_category_name, make_category_folder, Logger
from app.names import is_application, is_log
from app.messages import MSG_CONFIRM, MSG_MOVED, MSG_IGNORED


def main():
    working_folder = None

    if len(sys.argv) == 1:
        working_folder = get_working_folder()

    if not sg.popup_ok_cancel(MSG_CONFIRM(working_folder)):
        raise SystemExit("Cancelado, operação abortada.")

    destination_folder = make_destination_folder(working_folder)
    logger = Logger(working_folder)

    for file_name in os.listdir(working_folder):
        file = os.path.join(working_folder, file_name)
        if is_application(file_name) or is_log(file_name) or not os.path.isfile(file):
            continue
        file_extension = str.lower(os.path.splitext(file)[1])
        category_name = get_category_name(file_extension)
        category_folder = make_category_folder(destination_folder, category_name)
        try:
            shutil.move(file, category_folder)
            logger.log(MSG_MOVED(file_name, category_folder))
        except shutil.Error as e:
            logger.log(MSG_IGNORED(file_name))

    if sg.popup_ok("ARQUIVOS ORGANIZADOS!\nPRESSIONE OK PARA ABRIR PASTA ORGANIZADA"):
        os.startfile(os.path.realpath(destination_folder))
        return "CONCLUIDO!"


if __name__ == "__main__":
    main()
