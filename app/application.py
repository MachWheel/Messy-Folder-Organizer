# coding=utf-8
import json
import logging
from os import listdir

from resources.messages import EXTS_LOADED
from resources.names import EXTENSIONS_PATH
from .controller import Controller
from .filter import Filter
from .worker import Worker


class Application:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.controller = Controller()

    def running(self):
        return self.controller.read_events(self)


    def start(self, working_dir, make_subdir):
        work = Worker(working_dir, make_subdir)
        exts = self._load_extensions()
        check = Filter(working_dir, exts)
        for file in listdir(working_dir):
            if check.ignored_file(file):
                continue
            category = check.category_name(file)
            work.move_file(file, category)
        work.terminate()


    def _load_extensions(self) -> dict[str, list[str]]:
        with open(EXTENSIONS_PATH, "r") as extensions_file:
            self.log.debug(EXTS_LOADED)
            return json.load(extensions_file)
