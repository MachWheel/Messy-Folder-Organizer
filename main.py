# coding=utf-8
import logging.config

from controller import Controller
from resources import names, txt
from views import MAIN_WINDOW


def main(app: Controller):
    log = logging.getLogger(__name__)
    log.debug(txt.STARTED)
    while True:
        log.debug(txt.DRAWN(view))
        if app.read_events() == 'done':
            break

if __name__ == "__main__":
    logging.config.fileConfig(names.LOG_SETTINGS)
    logging.debug(txt.INITIALIZING)
    view = MAIN_WINDOW()
    main(Controller(view))
