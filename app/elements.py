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
    CONFIGURE_HELP, INFO_HELP, BROWSE_TOOLTIP, START_TOOLTIP
)
from resources.names import THEME

sg.theme(THEME)

_BTN_COLOR = sg.theme_background_color(), sg.theme_background_color()

MAIN_TEXT = sg.Text(SELECT_FOLDER, font="Default 14 bold", p=((10, 10), (20, 10)))

BROWSE_BTN = sg.B(button_type=BUTTON_TYPE_BROWSE_FOLDER,
                  image_data=icons.FOLDER(),
                  button_color=_BTN_COLOR,
                  border_width=0,
                  target='-IN-',
                  tooltip=BROWSE_TOOLTIP)

START_BTN = sg.B(button_type=BUTTON_TYPE_READ_FORM,
                 image_data=icons.START(),
                 button_color=_BTN_COLOR,
                 border_width=0,
                 tooltip=START_TOOLTIP,
                 key="-START_BTN-")

H_SEP = sg.HSep(p=((10, 10), (20, 10)))

INPUT = sg.In(k='-IN-', size=(30, 4), font="Default 14")

SUBDIR_CHECK = sg.CB(text=SUBDIR_CHECK, tooltip=SUBDIR_CHECK_TOOLTIP,
                     default=False, key='-SUBDIR_CHECK-')

CONFIG_BTN = sg.B(image_data=icons.CONFIGURE(),
                  button_color=_BTN_COLOR,
                  border_width=0,
                  tooltip=CONFIGURE_TOOLTIP,
                  key="-CONFIGURE_BTN-",
                  enable_events=True)

INFO_BTN = sg.B(image_data=icons.INFO(),
                button_color=_BTN_COLOR,
                border_width=0,
                key="-INFO_BTN-",
                enable_events=True)

OK = sg.B(image_data=icons.START(),
          button_color=_BTN_COLOR,
          border_width=0,
          key="-OK-")

MAIN_WINDOW = sg.Window(
    APP_TITLE,
    [
        [MAIN_TEXT],
        [BROWSE_BTN, INPUT, START_BTN],
        [H_SEP],
        [SUBDIR_CHECK, sg.Push(), CONFIG_BTN, INFO_BTN]
    ], finalize=True
)

def CONFIGURE_POPUP():
    return sg.popup_ok_cancel(CONFIGURE_HELP,
                              font="Default 14",
                              no_titlebar=True)

def INFO_POPUP():
    return sg.popup_yes_no(INFO_HELP,
                           font="Default 14",
                           no_titlebar=True)
