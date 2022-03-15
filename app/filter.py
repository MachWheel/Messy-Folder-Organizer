# coding=utf-8
import logging
from os.path import isfile, join, splitext

from resources.names import LOG_NAME


class Filter:
    def __init__(self, app, file_name):
        self.log = logging.getLogger(__name__)
        self.file_path = join(app.working_folder, file_name)
        self.file_name = splitext(file_name)[0]
        self.file_extension = str.lower(splitext(file_name)[1])
        self.extensions = app.extensions


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
        if not isfile(self.file_path) or self.is_log:
            return True
        return False


    @property
    def is_log(self) -> bool:
        return self.file_name == LOG_NAME
