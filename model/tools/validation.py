import re
import tkinter.messagebox as msg


def name_validator(value):
    if re.match(r"^[a-zA-Z\s]{3,30}$", value):
        return True, value
    else:
        raise ValueError("Invalid Name/Family")


def resident_count_validator(value):
    if 0 < int(value) < 9:
        return True, value
    else:
        raise ValueError("Invalid Resident Count")


def unit_number_validator(value):
    if 0 < int(value) <= 30:
        return True, value
    else:
        raise ValueError("Invalid Unit Number")


def expense_validator(value):
    if 0 < int(value) <= 1000000:
        return True, value
    else:
        raise ValueError("Invalid Expenses")


def month_validator(value):
    month_list = ['Farvardin', 'Ordibehesht', 'Khordad', 'Tir', 'Mordad', 'Shahrivar', 'Mehr', 'Aban', 'Azar', 'Dey', 'Bahman', 'Esfand']
    if value.capitalize() in month_list:
        return True, value
    else:
        raise ValueError("Invalid Month")