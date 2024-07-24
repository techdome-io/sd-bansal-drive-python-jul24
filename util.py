import re


def clean_string(s):
    return re.sub(r'\s+', '', s)
