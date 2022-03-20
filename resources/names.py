# coding=utf-8
import calendar
from datetime import datetime


def MONTH_YEAR():
    now = datetime.now()
    month_num = now.month
    month_name = calendar.month_name[month_num]
    return f"{month_name} {now.year}"

LOG_NAME = "app_log.log"

THEME = "DarkBlue"

IGNORED_CATEGORY = "Ignored"

OTHER_CATEGORY = "Other"

DONATE_LINK = "https://www.paypal.com/donate/?hosted_button_id=RNDCMNV4YWHX4"

EXTENSIONS_PATH = "resources/configs/extensions.json"
