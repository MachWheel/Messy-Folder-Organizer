import logging
import webbrowser
from os import startfile
from os.path import realpath

from PySimpleGUI import read_all_windows, WIN_CLOSED

from app.elements import CONFIGURE_POPUP, INFO_POPUP, CONFIRM_POPUP, ABORTED_POPUP
from resources.messages import CONFIRM, CANCELLED, CONFIRMED
from resources.names import EXTENSIONS_PATH, DONATE_LINK


class Controller:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def read_events(self, app):
        window, event, values = read_all_windows()

        if event == "-START_BTN-":
            working_dir = values["-IN-"]
            make_subdir = values["-SUBDIR_CHECK-"]
            if not self._start_check(working_dir):
                return
            app.start(working_dir, make_subdir)
            return 'done'

        if event == "-CONFIGURE_BTN-":
            if CONFIGURE_POPUP() == 'OK':
                startfile(realpath(EXTENSIONS_PATH))
                return 'done'

        if event == "-INFO_BTN-":
            window.hide()
            if INFO_POPUP() == 'Yes':
                webbrowser.open(DONATE_LINK, new=0)
            window.un_hide()

        if event == WIN_CLOSED:
            return 'done'


    def _start_check(self, working_dir):
        if not working_dir:
            return False
        msg = CONFIRM(working_dir)
        if CONFIRM_POPUP(msg) != 'OK':
            ABORTED_POPUP()
            self.log.info(CANCELLED)
            return False
        self.log.debug(CONFIRMED)
        return True
