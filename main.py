# coding=utf-8
import os
import shutil

import PySimpleGUI as sg

from app import get_working_folder, make_destination_folder, get_category_name, make_category_folder, Log, ignore_file
from app.messages import CANCELLED, CONFIRM, MOVED, IGNORED, DEST_FOLDER, DONE
from app.names import is_application, is_log


def main():
    working_folder = get_working_folder()
    log = Log(working_folder)

    if not sg.popup_ok_cancel(CONFIRM(working_folder)):
        raise SystemExit(CANCELLED)

    dest_folder, created = make_destination_folder(working_folder)
    log.msg(DEST_FOLDER(dest_folder, created))

    for file_name in os.listdir(working_folder):
        file = os.path.join(working_folder, file_name)
        if is_application(file_name) or is_log(file_name) or not os.path.isfile(file):
            continue
        file_extension = str.lower(os.path.splitext(file)[1])
        category_name = get_category_name(file_extension)
        if ignore_file(category_name):
            continue
        category_folder = make_category_folder(dest_folder, category_name)
        try:
            shutil.move(file, category_folder)
            log.msg(MOVED(file_name, category_folder))
        except shutil.Error as e:
            log.msg(IGNORED(file_name))
            log.msg(e)

    if sg.popup_ok(DONE):
        os.startfile(os.path.realpath(dest_folder))
        return


if __name__ == "__main__":
    main()
