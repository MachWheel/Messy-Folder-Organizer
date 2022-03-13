# coding=utf-8
import logging.config

from app import App
from app.factory import Factory


def main(application: App):
    application.start()


if __name__ == "__main__":
    logging.config.fileConfig("resource/log_config.ini")
    factory = Factory()
    main(factory.create_app())
