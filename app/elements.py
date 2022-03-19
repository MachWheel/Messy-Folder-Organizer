# coding=utf-8
import PySimpleGUI as sg
from PySimpleGUI import (
    BUTTON_TYPE_BROWSE_FOLDER,
    BUTTON_TYPE_READ_FORM
)

from resources import icons
from resources.messages import (
    APP_TITLE, SELECT_FOLDER, SUBDIR_CHECK,
    SUBDIR_CHECK_TOOLTIP, CONFIGURE_TOOLTIP,
    CONFIGURE_HELP, INFO_HELP, BROWSE_TOOLTIP,
    START_TOOLTIP, CANCELLED, DONE
)
from resources.names import THEME

sg.theme(THEME)

def MAIN_WINDOW():
    return sg.Window(
        APP_TITLE,
        [
            [_MAIN_TEXT],
            [_BROWSE_BTN, _INPUT, _START_BTN],
            [_H_SEP],
            [_SUBDIR_CHECK, sg.Push(), _CONFIG_BTN, _INFO_BTN]
        ], finalize=True
    )

def CONFIGURE_POPUP():
    return sg.popup_ok_cancel(CONFIGURE_HELP,
                              font=_MSG_FONT,
                              no_titlebar=True)

def INFO_POPUP():
    return sg.popup_yes_no(INFO_HELP,
                           font=_MSG_FONT,
                           no_titlebar=True)

def CONFIRM_POPUP(msg):
    return sg.popup_ok_cancel(msg,
                              font=_MSG_FONT,
                              no_titlebar=True)

def ABORTED_POPUP():
    return sg.popup(CANCELLED,
                    font=_MSG_FONT,
                    no_titlebar=True)

def DONE_POPUP():
    return sg.popup_ok(DONE,
                       font=_MSG_FONT,
                       no_titlebar=True)

_BTN_COLOR = sg.theme_background_color(), sg.theme_background_color()

_MSG_FONT = "Default 14"

_MAIN_TEXT = sg.Text(SELECT_FOLDER, font="Default 14 bold", p=((10, 10), (20, 10)))

_BROWSE_BTN = sg.B(button_type=BUTTON_TYPE_BROWSE_FOLDER,
                   image_data=icons.FOLDER(),
                   button_color=_BTN_COLOR,
                   border_width=0,
                   target='-IN-',
                   tooltip=BROWSE_TOOLTIP)

_START_BTN = sg.B(button_type=BUTTON_TYPE_READ_FORM,
                  image_data=icons.START(),
                  button_color=_BTN_COLOR,
                  border_width=0,
                  tooltip=START_TOOLTIP,
                  key="-START_BTN-")

_H_SEP = sg.HSep(p=((10, 10), (20, 10)))

_INPUT = sg.In(k='-IN-', size=(30, 4), font=_MSG_FONT)

_SUBDIR_CHECK = sg.CB(text=SUBDIR_CHECK, tooltip=SUBDIR_CHECK_TOOLTIP,
                      default=False, key='-SUBDIR_CHECK-')

_CONFIG_BTN = sg.B(image_data=icons.CONFIGURE(),
                   button_color=_BTN_COLOR,
                   border_width=0,
                   tooltip=CONFIGURE_TOOLTIP,
                   key="-CONFIGURE_BTN-",
                   enable_events=True)

_INFO_BTN = sg.B(image_data=icons.INFO(),
                 button_color=_BTN_COLOR,
                 border_width=0,
                 key="-INFO_BTN-",
                 enable_events=True)
