# coding=utf-8
from datetime import datetime
import calendar


def MONTH_YEAR():
    now = datetime.now()
    month_num = now.month - 1
    month_name = calendar.month_name[month_num]
    return f"{month_name} {now.year}"


LOG_NAME = (f"Log "
            f"{datetime.now().strftime('%m_%d_%Y at %H-%M')}.log")

THEME = "DarkBlue"

IGNORED_CATEGORY = "Ignored"

DONATE_LINK = "https://www.paypal.com/donate/?hosted_button_id=RNDCMNV4YWHX4"
