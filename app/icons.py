import base64

def START():
    with open("resource/icons/start.png", "rb") as png_file:
        return base64.b64encode(png_file.read())


def FOLDER():
    with open("resource/icons/folder.png", "rb") as png_file:
        return base64.b64encode(png_file.read())
