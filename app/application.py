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
    def __init__(self, extensions):
        self.log = logging.getLogger(__name__)
        self.extensions = extensions
        self.working_folder = None


    def run(self):
        window, event, values = sg.read_all_windows()

        if event == "-START_BTN-" and values["-IN-"]:
            self.working_folder = values["-IN-"]
            if not self._confirm_action():
                return
            self._work()
            return 'done'

        if event == sg.WIN_CLOSED:
            return 'done'


    def _work(self):
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
