# coding=utf-8
from app import App
from app.factory import Factory


def main(application: App):
    application.start()


if __name__ == "__main__":
    factory = Factory()
    main(factory.app())
