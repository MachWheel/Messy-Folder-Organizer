# coding=utf-8
import json
import logging

import PySimpleGUI as sg

from resources.messages import CANCELLED, WORKING, FACTORY, STARTED, EXTS_LOADED
from resources.names import THEME
from .application import Application
from .elements import MAIN_WINDOW


class Factory:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug(FACTORY)


    def create_app(self):
        extensions = self._load_extensions()
        working_folder = self._set_working_folder()
        self.log.debug(STARTED)
        return Application(working_folder, extensions)


    def _load_extensions(self) -> dict[str, list[str]]:
        with open("resources/configs/extensions.json", "r") as extensions_file:
            self.log.debug(EXTS_LOADED)
            return json.load(extensions_file)


    def _set_working_folder(self) -> str:
        sg.theme(THEME)
        working_folder = MAIN_WINDOW.read(close=True)[1]['-IN-']
        if not working_folder:
            self._abort_operation()
        self.log.info(WORKING(working_folder))
        return working_folder


    def _abort_operation(self):
        sg.popup(CANCELLED)
        self.log.info(CANCELLED)
        raise SystemExit(CANCELLED)
