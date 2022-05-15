import json
import logging
import shutil
from os import mkdir, path, startfile
from os.path import join, splitext, isfile

import views
from shared import files, txt


class Organizer:
    def __init__(self, working_dir, make_subdir: bool):
        self.log = logging.getLogger(__name__)
        self.working_dir = working_dir
        self.output_dir = working_dir
        if make_subdir:
            subdir = f"{working_dir}/{txt.MONTH_YEAR()}"
            self.output_dir = self._make_folder(subdir)
        self.log.info(txt.WORKING_AT(working_dir))
        with open(files.EXTENSIONS, "r") as extensions_file:
            self.extensions = json.load(extensions_file)
            self.log.debug(txt.EXTS_LOADED)


    def move_file(self, file, category_name) -> None:
        file_path = f"{self.working_dir}/{file}"
        dir_path = f"{self.output_dir}/{category_name}"
        category_folder = self._make_folder(dir_path)
        try:
            shutil.move(file_path, category_folder)
            self.log.info(txt.MOVED(file, category_folder))
        except shutil.Error as e:
            self.log.error(txt.IGNORED(file))
            self.log.error(e)


    def terminate(self) -> str:
        if views.DONE_POPUP():
            startfile(path.realpath(self.output_dir))
            self.log.debug(txt.FINISHED)
            startfile(files.LOG)
            return 'done'


    def get_category(self, file) -> str:
        file_extension = str.lower(splitext(file)[1])
        for category, entries in self.extensions.items():
            if file_extension in entries:
                name = category.capitalize()
                return name
        return txt.OTHER_CATEGORY


    def ignored_file(self, file) -> bool:
        file_path = join(self.working_dir, file)
        file_name = splitext(file)[0]
        return not isfile(file_path) \
               or file_name == files.LOG \
               or self.get_category(file) == txt.IGNORED_CATEGORY


    def _make_folder(self, folder_path) -> str:
        try:
            mkdir(folder_path)
            self.log.info(txt.CREATED(folder_path))
        except FileExistsError:
            self.log.debug(txt.EXISTING(folder_path))
            pass
        return folder_path
