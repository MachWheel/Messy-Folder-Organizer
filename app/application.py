# coding=utf-8

import logging
import webbrowser
from os import startfile, listdir
from os.path import realpath

import PySimpleGUI as sg

from resources.messages import (
    CANCELLED, CONFIRM, CONFIRMED,
    WORKING
)
from resources.names import (
    DONATE_LINK, EXTENSIONS_PATH
)
from .elements import (
    CONFIGURE_POPUP, INFO_POPUP,
    CONFIRM_POPUP, ABORTED_POPUP
)
from .filter import Filter
from .worker import Worker


class Application:
    def __init__(self, extensions):
        self.log = logging.getLogger(__name__)
        self.extensions = extensions


    def run(self):
        window, event, values = sg.read_all_windows()

        if event == "-START_BTN-":
            work_on = values["-IN-"]
            make_subdir = values["-SUBDIR_CHECK-"]
            return self._start(work_on, make_subdir)

        if event == "-CONFIGURE_BTN-":
            if CONFIGURE_POPUP() == 'OK':
                startfile(realpath(EXTENSIONS_PATH))
                return 'done'

        if event == "-INFO_BTN-":
            window.hide()
            if INFO_POPUP() == 'Yes':
                webbrowser.open(DONATE_LINK, new=0)
            window.un_hide()

        if event == sg.WIN_CLOSED:
            return 'done'


    def _start(self, work_on, make_subdir):
        if not work_on:
            return
        self.working_folder = work_on
        if not self._confirm_action():
            return
        self._work(make_subdir)
        return 'done'


    def _work(self, make_subdir):
        msg = WORKING(self.working_folder)
        self.log.info(msg)
        worker = Worker(self.working_folder, make_subdir)
        for file_name in listdir(self.working_folder):
            f = Filter(self, file_name)
            if f.ignored_file:
                continue
            worker.move_file(f)
        worker.terminate()


    def _confirm_action(self):
        msg = CONFIRM(self.working_folder)
        if CONFIRM_POPUP(msg) != 'OK':
            ABORTED_POPUP()
            self.log.info(CANCELLED)
            return False
        self.log.debug(CONFIRMED)
        return True
