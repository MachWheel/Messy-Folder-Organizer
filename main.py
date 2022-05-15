import logging.config

import seed
from controller import Controller
from shared import files, txt
from views import MAIN_WINDOW


def main(app: Controller):
    log = logging.getLogger(__name__)
    log.debug(txt.STARTED)
    while True:
        log.debug(txt.DRAWN(view))
        if app.read_events() == 'done':
            break

if __name__ == "__main__":
    seed.make_config_files()
    # seed.update()  # COMMENT BEFORE COMPILING
    logging.config.fileConfig(files.LOG_CONFIG)
    logging.debug(txt.INITIALIZING)
    view = MAIN_WINDOW()
    main(Controller(view))
