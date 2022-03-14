# coding=utf-8
import logging

import PySimpleGUI as sg

from . import App
from .elements import BROWSE, START, TEXT, INPUT
from .messages import APP_TITLE, CANCELLED, WORKING, FACTORY, STARTED
from .names import THEME


class Factory:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug(FACTORY)


    def create_app(self):
        working_folder = self.get_working_folder()
        self.log.debug(STARTED)
        return App(working_folder)


    def get_working_folder(self) -> str:
        sg.theme(THEME)
        working_folder = sg.Window(
            APP_TITLE,
            [
                [TEXT],
                [BROWSE, INPUT, START]
            ], size=(480, 150)
        ).read(close=True)[1]['-IN-']

        if not working_folder:
            sg.popup(CANCELLED)
            self.log.info(CANCELLED)
            raise SystemExit(CANCELLED)

        self.log.info(WORKING(working_folder))
        return working_folder
