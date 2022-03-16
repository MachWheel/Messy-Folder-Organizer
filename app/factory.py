# coding=utf-8
import json
import logging

from resources.messages import FACTORY, EXTS_LOADED
from .application import Application
from .elements import MAIN_WINDOW


class Factory:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug(FACTORY)


    def create_app(self):
        extensions = self._load_extensions()
        return Application(extensions), MAIN_WINDOW


    def _load_extensions(self) -> dict[str, list[str]]:
        with open("resources/configs/extensions.json", "r") as extensions_file:
            self.log.debug(EXTS_LOADED)
            return json.load(extensions_file)
