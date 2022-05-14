import PySimpleGUI as sg

from resources import txt, names
from . import _icons


def HEADING():
    return sg.T(
        txt.SELECT_FOLDER,
        font="Default 14 bold",
        p=((10, 10), (20, 10))
    )


def BROWSE_BTN():
    return sg.B(
        button_type=sg.BUTTON_TYPE_BROWSE_FOLDER,
        image_data=_icons.FOLDER,
        button_color=_icons.BTN_COLOR(),
        border_width=0,
        target='-IN-',
        tooltip=txt.BROWSE_TOOLTIP
    )


def START_BTN():
    return sg.B(
        button_type=sg.BUTTON_TYPE_READ_FORM,
        image_data=_icons.START,
        button_color=_icons.BTN_COLOR(),
        border_width=0,
        tooltip=txt.START_TOOLTIP,
        key="-START_BTN-"
    )


def SEPARATOR():
    return sg.HSep(p=((10, 10), (20, 10)))


def FOLDER_INPUT():
    settings = sg.UserSettings(names.SETTINGS_FILE, names.SETTINGS_PATH)
    return sg.In(
        default_text=settings.get('-IN-', ''),
        key='-IN-',
        size=(30, 4),
        font=txt.MSG_FONT
    )


def SUBDIR_CHECK():
    settings = sg.UserSettings(names.SETTINGS_FILE, names.SETTINGS_PATH)
    return sg.CB(
        text=txt.SUBDIR_CHECK,
        default=settings.get('-SUBDIR_CHECK-', False),
        tooltip=txt.SUBDIR_CHECK_TOOLTIP,
        key='-SUBDIR_CHECK-'
    )


def CONFIG_BTN():
    return sg.B(
        image_data=_icons.CONFIGURE,
        button_color=_icons.BTN_COLOR(),
        border_width=0,
        tooltip=txt.CONFIGURE_TOOLTIP,
        key="-CONFIGURE_BTN-",
        enable_events=True
    )


def INFO_BTN():
    return sg.B(
        image_data=_icons.INFO,
        button_color=_icons.BTN_COLOR(),
        border_width=0,
        key="-INFO_BTN-",
        enable_events=True
    )
