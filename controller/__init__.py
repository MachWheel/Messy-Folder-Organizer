import logging
import webbrowser
from os import startfile, listdir
from os.path import realpath, isdir

import PySimpleGUI as sg

import views
from shared import files, txt
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
            self.view.hide()
            if not self._validate_input(working_dir):
                self.view.un_hide()
                return
            self.organize(working_dir, make_subdir)
            return 'done'

        if event == "-CONFIGURE_BTN-":
            if views.CONFIGURE_POPUP() == 'OK':
                startfile(realpath(files.EXTENSIONS))
                return 'done'

        if event == "-INFO_BTN-":
            self.view.hide()
            if views.INFO_POPUP() == 'Yes':
                webbrowser.open(txt.DONATE_LINK, new=0)
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


    def _validate_input(self, working_dir):
        folder = working_dir
        if not folder or not isdir(folder):
            views.ERROR_POPUP(txt.INVALID(folder))
            return False
        msg = txt.CONFIRM(working_dir)
        if views.CONFIRM_POPUP(msg) == 'OK':
            self.log.debug(txt.CONFIRMED)
            return True
        views.ABORTED_POPUP()
        self.log.info(txt.CANCELLED)
        return False


    @staticmethod
    def _save_settings(values):
        if not values:
            return
        file, path = files.SG_CONFIG, files.DIR_CONFIG
        settings = sg.UserSettings(file, path)
        values.pop('', None)
        settings.write_new_dictionary(values)
