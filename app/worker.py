import logging
import shutil
from os import mkdir, path, startfile

from resources.messages import (
    CREATED, DESTINATION, MOVED, IGNORED,
    EXISTING, FINISHED
)
from resources.names import MONTH_YEAR
from .elements import DONE_POPUP
from .filter import Filter

class Worker:
    def __init__(self, working_dir, make_subdir: bool):
        self.log = logging.getLogger(__name__)
        if make_subdir:
            self.output_folder = f"{working_dir}/{MONTH_YEAR()}"
            self._make_output_folder()
        else:
            self.output_folder = working_dir


    def _make_output_folder(self) -> None:
        try:
            mkdir(self.output_folder)
            self.log.info(CREATED(self.output_folder))
        except FileExistsError:
            pass
        self.log.info(DESTINATION(self.output_folder))


    def _make_folder(self, name) -> str:
        new_folder = f"{self.output_folder}/{name}"
        try:
            mkdir(new_folder)
            self.log.info(CREATED(new_folder))
        except FileExistsError:
            self.log.debug(EXISTING(new_folder))
            pass
        return new_folder


    def move_file(self, f: Filter) -> None:
        category_folder = self._make_folder(f.category_name)
        try:
            shutil.move(f.file_path, category_folder)
            self.log.info(MOVED(f))
        except shutil.Error as e:
            self.log.error(IGNORED(f))
            self.log.error(e)


    def terminate(self) -> str:
        if DONE_POPUP():
            startfile(path.realpath(self.output_folder))
            self.log.debug(FINISHED)
            startfile('app_log.log')
            return 'done'
