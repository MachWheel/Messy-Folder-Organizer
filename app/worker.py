import logging
import shutil
from os import mkdir, path, startfile
from os.path import join

from resources.messages import (
    CREATED, DESTINATION, MOVED, IGNORED,
    EXISTING, FINISHED, WORKING
)
from resources.names import MONTH_YEAR
from .elements import DONE_POPUP


class Worker:
    def __init__(self, working_dir, make_subdir: bool):
        self.log = logging.getLogger(__name__)
        if make_subdir:
            self.output_dir = f"{working_dir}/{MONTH_YEAR()}"
            self._make_output_folder()
        else:
            self.output_dir = working_dir
        self.log.info(WORKING(working_dir))


    def move_file(self, file, category_name) -> None:
        category = self._make_folder(category_name)
        file_path = join(self.output_dir, file)
        try:
            shutil.move(file_path, category)
            self.log.info(MOVED(file, category))
        except shutil.Error as e:
            self.log.error(IGNORED(file))
            self.log.error(e)


    def terminate(self) -> str:
        if DONE_POPUP():
            startfile(path.realpath(self.output_dir))
            self.log.debug(FINISHED)
            startfile('app_log.log')
            return 'done'


    def _make_output_folder(self) -> None:
        try:
            mkdir(self.output_dir)
            self.log.info(CREATED(self.output_dir))
        except FileExistsError:
            pass
        self.log.info(DESTINATION(self.output_dir))


    def _make_folder(self, name) -> str:
        new_folder = f"{self.output_dir}/{name}"
        try:
            mkdir(new_folder)
            self.log.info(CREATED(new_folder))
        except FileExistsError:
            self.log.debug(EXISTING(new_folder))
            pass
        return new_folder
