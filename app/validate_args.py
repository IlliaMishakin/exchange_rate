import re

from config import DATE_PATTERN


def validate_date_format(date_string):
    if re.match(DATE_PATTERN, date_string):
        return True
    else:
        return False