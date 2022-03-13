# coding=utf-8
import logging

import PySimpleGUI as sg

from . import App
from .messages import APP_TITLE, CANCELLED, SELECT_FOLDER, WORKING, FACTORY, STARTED


class Factory:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug(FACTORY)


    def create_app(self):
        working_folder = self.get_working_folder()
        self.log.debug(STARTED)
        return App(working_folder)


    def get_working_folder(self) -> str:
        working_folder = sg.Window(
            APP_TITLE,
            [
                [sg.Text(SELECT_FOLDER)],
                [sg.In(), sg.FolderBrowse()],
                [sg.Open(), sg.Cancel()]
            ]
        ).read(close=True)[1][0]
        if not working_folder:
            sg.popup(CANCELLED)
            self.log.info(CANCELLED)
            raise SystemExit(CANCELLED)
        self.log.info(WORKING(working_folder))
        return working_folder
