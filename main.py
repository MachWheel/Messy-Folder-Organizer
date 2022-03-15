# coding=utf-8
import logging.config

from app.application import Application
from app.factory import Factory


def main(app: Application):
    app.start()


if __name__ == "__main__":
    logging.config.fileConfig("resources/configs/log_config.ini")
    factory = Factory()
    main(factory.create_app())
