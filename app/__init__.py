# coding=utf-8
import logging
import os
import shutil
from os import mkdir

import PySimpleGUI as sg

from .filter import Filter
from .messages import (
    APP_TITLE, CANCELLED, CREATED, SELECT_FOLDER, DESTINATION,
    MOVED, IGNORED, DONE, CONFIRM, CONFIRMED, EXISTING, FINISHED
)
from .names import MES_ANO, LOG_NAME


class App:
    def __init__(self, working_folder):
        self.log = logging.getLogger(__name__)
        self.working_folder = working_folder
        self.destination_folder = None


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
            self.log.info(CANCELLED)
            return False
        self.log.debug(CONFIRMED)
        return True


    def make_destination_folder(self) -> None:
        dest_folder = f"{self.working_folder}/{MES_ANO()}"
        try:
            mkdir(dest_folder)
            self.log.info(CREATED(dest_folder))
        except FileExistsError:
            pass
        self.destination_folder = dest_folder
        self.log.info(DESTINATION(dest_folder))


    def move_file(self, f: Filter):
        category_folder = self.make_category_folder(f.category_name)
        try:
            shutil.move(f.file, category_folder)
            self.log.info(MOVED(f))
        except shutil.Error as e:
            self.log.error(IGNORED(f))
            self.log.error(e)


    def make_category_folder(self, category_name) -> str:
        category_folder = f"{self.destination_folder}/{category_name}"
        try:
            mkdir(category_folder)
            self.log.info(CREATED(category_folder))
        except FileExistsError:
            self.log.debug(EXISTING(category_folder))
            pass
        return category_folder


    def done_moving(self) -> None:
        if sg.popup_ok(DONE):
            os.startfile(os.path.realpath(self.destination_folder))
            self.log.debug(FINISHED)
            os.startfile(LOG_NAME)
            return
