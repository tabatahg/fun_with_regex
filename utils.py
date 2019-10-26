"""utilities"""
import re


def isNumberRegex(value):
    not_integer = re.compile(r'\D')
    number_check = not_integer.search(value.strip())
    if number_check is None:
        convert_number = int(value)
        return convert_number
    else:
        return value


"""Test"""
# print(isNumberRegex(input("input something:")))
