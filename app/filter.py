# coding=utf-8
import json
from os import path

from .names import log_name


class Filter:
    def __init__(self, working_folder, file_name):
        self.file = path.join(working_folder, file_name)
        self.file_name = path.splitext(file_name)[0]
        self.file_extension = str.lower(path.splitext(self.file)[1])


    @property
    def extensions(self) -> dict[str, list[str]]:
        with open("app/extensions.json", "r") as extensions_file:
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
        if not path.isfile(self.file):
            return True
        if self.is_application or self.is_log:
            return True
        return False


    @property
    def is_application(self) -> bool:
        app_path = path.basename(path.realpath(__file__))
        app_name = path.splitext(app_path)[0]
        print(f"APP_NAME: {app_name}")  # TESTING
        return self.file_name == app_name


    @property
    def is_log(self) -> bool:
        return self.file_name == log_name
