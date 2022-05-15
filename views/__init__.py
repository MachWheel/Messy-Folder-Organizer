import PySimpleGUI as sg

from . import _icons
from . import _gui

from shared import txt


def MAIN_WINDOW():
    sg.theme(txt.THEME)
    return sg.Window(
        txt.APP_TITLE,
        [
            [_gui.HEADING()],
            [_gui.BROWSE_BTN(), _gui.FOLDER_INPUT(), _gui.START_BTN()],
            [_gui.SEPARATOR()],
            [_gui.SUBDIR_CHECK(), sg.Push(), _gui.CONFIG_BTN(), _gui.INFO_BTN()]
        ]
    )


def CONFIGURE_POPUP():
    return sg.popup_ok_cancel(txt.CONFIGURE_HELP, font=txt.MSG_FONT, no_titlebar=True)


def INFO_POPUP():
    return sg.popup_yes_no(txt.INFO_HELP, font=txt.MSG_FONT, no_titlebar=True)


def CONFIRM_POPUP(msg):
    return sg.popup_ok_cancel(msg, font=txt.MSG_FONT, no_titlebar=True)


def ABORTED_POPUP():
    return sg.popup(txt.CANCELLED, font=txt.MSG_FONT, no_titlebar=True)


def DONE_POPUP():
    return sg.popup_ok(txt.DONE, font=txt.MSG_FONT, no_titlebar=True)


def ERROR_POPUP(msg):
    return sg.popup_error(msg, font=txt.MSG_FONT, no_titlebar=True)
