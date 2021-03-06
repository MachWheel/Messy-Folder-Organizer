import calendar
from datetime import datetime


def CONFIRM(working_folder):
    return (f"\nFiles inside the selected folder:"
            f"\n\n"
            f"{working_folder}"
            f"\n\n"
            f"are going to be moved based on "
            f"their types."
            f"\n\n"
            f"DO YOU WISH TO CONTINUE?\n")


def MOVED(file, destination):
    return f"\n[#] FILE '{file}' MOVED TO: '{destination}'\n"


def IGNORED(file):
    return f"\n[!] FILE '{file}' IGNORED."


def EXISTING(folder):
    return f"\n[!] USING EXISTING FOLDER:\n'{folder}'\n"


def CREATED(folder):
    return f"\n[#] FOLDER '{folder}' CREATED.\n"


def WORKING_AT(folder):
    return f"\n[#] WORKING FOLDER:\n'{folder}'\n"


def DRAWN(view):
    return f"\nDRAWN WINDOW: {view}\n"

def INVALID(folder):
    return f"\nYou have chosen an invalid folder to organize:\n{folder}\n"

APP_TITLE = 'Messy Folder Organizer v1.3'

INITIALIZING = '\nCREATING APPLICATION...\n'

STARTED = '\nAPPLICATION INITIALIZED.\n'


BROWSE_TOOLTIP = "Choose folder"

START_TOOLTIP = "Start organizing"

MSG_FONT = "Default 14"

THEME = "DarkBlue"

IGNORED_CATEGORY = "Ignored"

OTHER_CATEGORY = "Other"

DONATE_LINK = "https://www.paypal.com/donate/?hosted_button_id=RNDCMNV4YWHX4"

SELECT_FOLDER = 'Choose a messy folder to organize:'

DONE = (f"\nFOLDER ORGANIZED!\n"
        f"PRESS OK TO OPEN IT.\n\n"
        f"The log file will also "
        f"open so you can see which "
        f"files were moved and where.\n\n"
        f"Have a great day!\n")

EXTS_LOADED = "\nEXTENSIONS LOADED.\n"

CANCELLED = "\n\nOPERATION ABORTED.\n\n"

CONFIRMED = "\nOPERATION CONFIRMED.\n"

FINISHED = '\nOPERATION FINISHED.\n'


def MONTH_YEAR():
    now = datetime.now()
    month_num = now.month
    month_name = calendar.month_name[month_num]
    return f"{month_name} {now.year}"


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
             "(International) Paypal - just press Yes\n"
             "(Brazil) Chave PIX: wyllerhacks@gmail.com\n\n"
             "Press Yes to open paypal.\n"
             "Press No to return.\n")
