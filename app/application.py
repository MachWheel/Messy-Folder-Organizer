# coding=utf-8

import logging
import webbrowser
from os import startfile, listdir
from os.path import realpath

import PySimpleGUI as sg

from resources.messages import (
    CANCELLED, CONFIRM, CONFIRMED, WORKING
)
from resources.names import DONATE_LINK
from .elements import CONFIGURE_POPUP, INFO_POPUP
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
            return self._start(
                work_on=values["-IN-"],
                make_subdir=values["-SUBDIR_CHECK-"])

        if event == "-CONFIGURE_BTN-":
            if CONFIGURE_POPUP() == 'OK':
                startfile(realpath("resources/configs/extensions.json"))
                return 'done'

        if event == "-INFO_BTN-":
            window.hide()
            if INFO_POPUP() == 'Yes':
                webbrowser.open(DONATE_LINK, new=0)
            window.un_hide()

        if event == sg.WIN_CLOSED:
            return 'done'


    def _start(self, work_on, make_subdir):
        self.working_folder = work_on
        if not self._confirm_action():
            return
        self._work(make_subdir)
        return 'done'


    def _work(self, subdir):
        self.log.info(WORKING(self.working_folder))
        worker = Worker(self.working_folder, subdir)
        for file_name in listdir(self.working_folder):
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
