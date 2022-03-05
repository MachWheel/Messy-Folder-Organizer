# coding=utf-8
import PySimpleGUI as sg

from . import App
from .messages import APP_TITLE, CANCELLED, SELECT_FOLDER


class Factory:
    def app(self):
        working_folder = self.get_working_folder()
        return App(working_folder)


    @staticmethod
    def get_working_folder() -> str:
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
            raise SystemExit(CANCELLED)
        return working_folder
