import re

def reg_check(phone_num, mesg):
    pattern_1 = "^\+?[0-9]{2}?[0-9]{6,12}$"
    msg_pattern = "^[a-zA-Z ]{1,250}$"
    phone_check = re.compile(pattern_1)
    msg_check = re.compile(msg_pattern)

    if (re.search(phone_check, phone_num)) and (re.search(msg_check, mesg)):
        return True
    else:
        return False
print(reg_check("+919994408342","Hi from vinith"))
