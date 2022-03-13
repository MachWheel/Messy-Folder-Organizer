# coding=utf-8
import json
import logging
from os import path

from .messages import EXTS_LOADED
from .names import LOG_NAME


class Filter:
    def __init__(self, working_folder, file_name):
        self.log = logging.getLogger(__name__)
        self.file = path.join(working_folder, file_name)
        self.file_name = path.splitext(file_name)[0]
        self.file_extension = str.lower(path.splitext(self.file)[1])


    @property
    def extensions(self) -> dict[str, list[str]]:
        with open("resource/extensions.json", "r") as extensions_file:
            self.log.debug(EXTS_LOADED)
            return json.load(extensions_file)


    @property
    def category_name(self) -> str:
        for category, entries in self.extensions.items():
            if self.file_extension in entries:
                name = category.capitalize()
                return name
        return "Outros"


    @property
    def ignored_category(self):
        return True if self.category_name == "Ignorados" else False


    @property
    def ignored_file(self):
        if not path.isfile(self.file) or self.is_log:
            return True
        return False


    @property
    def is_log(self) -> bool:
        return self.file_name == LOG_NAME