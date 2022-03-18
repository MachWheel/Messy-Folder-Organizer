# coding=utf-8
import logging.config

from PySimpleGUI import Window

from app.application import Application
from app.factory import Factory
from resources.messages import DRAWN, STARTED


def main(app: Application, view: Window):
    log = logging.getLogger(__name__)
    log.debug(STARTED)
    while True:
        log.debug(DRAWN(view))
        status = app.run()
        if status == 'done':
            break


if __name__ == "__main__":
    logging.config.fileConfig("resources/configs/log_config.ini")
    factory = Factory()
    main(*factory.create_app())
