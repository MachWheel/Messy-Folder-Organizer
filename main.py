# coding=utf-8
import logging

from app import App
from app.factory import Factory
from app.names import LOG_NAME


def main(application: App):
    application.start()


if __name__ == "__main__":
    # noinspection PyArgumentList
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
        filename=LOG_NAME,
        filemode='w',
        encoding='utf-8'
    )
    factory = Factory()
    main(factory.create_app())
