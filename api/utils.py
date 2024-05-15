import re


# I chose to parse out a subset of the astronomical object notations
#  that are commonly used in the astronomy community.
def find_astronomical_object(text):
    pattern = r"(NGC|LEDA|IC)\s?\d{1,5}"
    match = re.search(pattern, text)
    if match:
        return match.group()
    else:
        return None
