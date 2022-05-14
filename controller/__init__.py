import logging
import webbrowser
from os import startfile, listdir
from os.path import realpath

import PySimpleGUI as sg

import views
from resources import names, txt
from .organizer import Organizer


class Controller:
    def __init__(self, view: sg.Window):
        self.log = logging.getLogger(__name__)
        self.view = view


    def read_events(self):
        event, values = self.view.read()

        if event == "-START_BTN-":
            working_dir = values["-IN-"]
            make_subdir = values["-SUBDIR_CHECK-"]
            self._save_settings(values)
            if not self._start_check(working_dir):
                return
            self.organize(working_dir, make_subdir)
            return 'done'

        if event == "-CONFIGURE_BTN-":
            if views.CONFIGURE_POPUP() == 'OK':
                startfile(realpath(names.EXTENSIONS_PATH))
                return 'done'

        if event == "-INFO_BTN-":
            self.view.hide()
            if views.INFO_POPUP() == 'Yes':
                webbrowser.open(names.DONATE_LINK, new=0)
            self.view.un_hide()

        if event == sg.WIN_CLOSED:
            return 'done'


    @staticmethod
    def organize(working_dir, make_subdir):
        worker = Organizer(working_dir, make_subdir)
        for file in listdir(working_dir):
            if worker.ignored_file(file):
                continue
            category = worker.get_category(file)
            worker.move_file(file, category)
        worker.terminate()


    def _start_check(self, working_dir):
        if not working_dir:
            return False
        msg = txt.CONFIRM(working_dir)
        if views.CONFIRM_POPUP(msg) != 'OK':
            views.ABORTED_POPUP()
            self.log.info(txt.CANCELLED)
            return False
        self.log.debug(txt.CONFIRMED)
        return True


    @staticmethod
    def _save_settings(values):
        if not values:
            return
        file, path = names.SETTINGS_FILE, names.SETTINGS_PATH
        settings = sg.UserSettings(file, path)
        values.pop('', None)
        settings.write_new_dictionary(values)
