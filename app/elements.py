import PySimpleGUI as sg
from PySimpleGUI import BUTTON_TYPE_BROWSE_FOLDER, BUTTON_TYPE_READ_FORM

from resources import icons
from resources.messages import APP_TITLE, SELECT_FOLDER, DONE
from resources.names import THEME

sg.theme(THEME)

_COLOR = sg.theme_background_color(), sg.theme_background_color()

TEXT = sg.Text(SELECT_FOLDER, font="Default 14 bold", p=((10, 10), (20, 10)))


BROWSE = sg.B(button_type=BUTTON_TYPE_BROWSE_FOLDER,
              image_data=icons.FOLDER(),
              button_color=_COLOR,
              border_width=0,
              target='-IN-',
              tooltip="ESCOLHER PASTA")


START = sg.B(button_type=BUTTON_TYPE_READ_FORM,
             image_data=icons.START(),
             button_color=_COLOR,
             tooltip="ORGANIZAR")


INPUT = sg.In(k='-IN-', size=(30, 4), font="Default 14")


MAIN_WINDOW = sg.Window(
    APP_TITLE,
    [
        [TEXT],
        [BROWSE, INPUT, START]
    ], size=(480, 150)
)
