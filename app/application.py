# coding=utf-8

import logging
import os

import PySimpleGUI as sg

from resources.messages import (
    CANCELLED, CONFIRM, CONFIRMED
)
from .filter import Filter
from .worker import Worker


class Application:
    def __init__(self, working_folder, extensions):
        self.log = logging.getLogger(__name__)
        self.working_folder = working_folder
        self.destination_folder = None
        self.extensions = extensions


    def start(self):
        if not self._confirm_action():
            return
        worker = Worker(self)
        for file_name in os.listdir(self.working_folder):
            f = Filter(self, file_name)
            if f.ignored_file:
                continue
            worker.move_file(f)
        worker.terminate()


    def _confirm_action(self):
        confirm = sg.popup_ok_cancel(CONFIRM(self.working_folder))
        if confirm != 'OK':
            sg.popup(CANCELLED)
            self.log.info(CANCELLED)
            return False
        self.log.debug(CONFIRMED)
        return True
