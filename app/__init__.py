# coding=utf-8
import os
import shutil
from os import mkdir

import PySimpleGUI as sg

from .filter import Filter
from .messages import APP_TITLE, CANCELLED, CREATED, SELECT_FOLDER, DESTINATION, MOVED, IGNORED, DONE, CONFIRM
from .names import mes_ano, log_name


class App:
    def __init__(self, working_folder):
        self.working_folder = working_folder
        self.destination_folder = None
        self.log_file = f"{self.working_folder}/{log_name}.txt"


    def start(self):
        if not self.confirm_action():
            return
        self.make_destination_folder()
        for file_name in os.listdir(self.working_folder):
            f = Filter(self.working_folder, file_name)
            if f.ignored_file:
                continue
            self.move_file(f)
        self.done_moving()


    def confirm_action(self):
        confirm = sg.popup_ok_cancel(CONFIRM(self.working_folder))
        if confirm != 'OK':
            sg.popup(CANCELLED)
            return False
        return True


    def make_destination_folder(self) -> None:
        dest_folder = f"{self.working_folder}/{mes_ano()}"
        try:
            mkdir(dest_folder)
            self.log(CREATED(dest_folder))
        except FileExistsError:
            pass
        self.destination_folder = dest_folder
        self.log(DESTINATION(dest_folder))


    def log(self, message) -> None:
        with open(self.log_file, 'a') as log_file:
            log_file.write(message)
            print(message)


    def move_file(self, f: Filter):
        category_folder = self.make_category_folder(f.category_name)
        try:
            shutil.move(f.file, category_folder)
            self.log(MOVED(f))
        except shutil.Error as e:
            self.log(IGNORED(f))
            self.log(e)


    def make_category_folder(self, category_name) -> str:
        category_folder = f"{self.destination_folder}/{category_name}"
        try:
            mkdir(category_folder)
            self.log(CREATED(category_folder))
        except FileExistsError:
            pass
        return category_folder


    def done_moving(self) -> None:
        if sg.popup_ok(DONE):
            os.startfile(os.path.realpath(self.destination_folder))
            os.startfile(os.path.realpath(self.log_file))
            return
