# coding=utf-8
from resources.names import MONTH_YEAR


def CONFIRM(working_folder):
    return (f"Files inside the selected folder:"
            f"\n'{working_folder}'\n"
            f"Will be organized accordingly "
            f"with their types.\n\n"
            f"DO YOU WISH TO CONTINUE?")


def MOVED(f):
    return f"\n[#] FILE '{f.file_name}{f.file_extension}' MOVED TO: '{f.category_name}'\n"


def IGNORED(f):
    return f"\n[!] FILE '{f.file_name}{f.file_extension}' IGNORED."


def DESTINATION(folder):
    return f"\n[!] FILES BEING MOVED TO:\n'{folder}'\n"


def EXISTING(folder):
    return f"\n[!] USING EXISTING FOLDER:\n'{folder}'\n"


def CREATED(folder):
    return f"\n[#] FOLDER '{folder}' CREATED.\n"


def WORKING(folder):
    return f"\n[#] WORKING IN FOLDER:\n'{folder}'\n"


def DRAWN(view):
    return f"\nDRAWN WINDOW: {view}\n"


APP_TITLE = 'Messy Folder Organizer'

FACTORY = '\nCREATING APPLICATION...\n'

STARTED = '\nAPPLICATION INITIALIZED.\n'

SELECT_FOLDER = 'Choose a messy folder to organize:'

DONE = (f"\nFOLDER ORGANIZED!\n"
        f"PRESS OK TO OPEN IT.\n\n"
        f"The log file will also "
        f"open so you can see which "
        f"files were moved and where.\n\n"
        f"Have a great day!\n")

EXTS_LOADED = "\nEXTENSIONS LOADED.\n"

CANCELLED = "\nOPERATION ABORTED.\n"

CONFIRMED = "\nOPERATION CONFIRMED.\n"

FINISHED = '\nOPERATION FINISHED.\n'

SUBDIR_CHECK = f'Organize files in subfolder "{MONTH_YEAR()}"'

SUBDIR_CHECK_TOOLTIP = "If unchecked, files will be organized inside the selected folder."

CONFIGURE_TOOLTIP = "Change extensions detected by the application"

CONFIGURE_HELP = ("\nYou can change extensions detected by the application!"
                  "\n\n"
                  "Just change the .json file that will be opened and save it.\n"
                  "Then, restart the application."
                  "\n\n"
                  "You can add new categories or change existing ones the way "
                  "you like it."
                  "\n\n"
                  "(Just don't change the name of ignored category, but feel "
                  "free to add new extensions to it.)"
                  "\n\n"
                  "Do you wish to proceed?\n")

INFO_HELP = ("\nHey! Was I of any help?\n"
             "A coffee would be nice =)\n\n"
             "(International) Paypal - click here to open!\n"
             "(Brazil) Chave PIX: wyllerhacks@gmail.com\n")
