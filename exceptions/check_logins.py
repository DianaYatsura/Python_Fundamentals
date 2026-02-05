#Write code inside function check.
#This function must check logins of some workers. We have 2 roles: there are "admin" and "employee",
# each login must contain role and id.
#Id is any natural number. Id and role may be separated by "-" or "-id" or "id".
#If function check obtain incorrect data (as example 'abc') it needs to raise ValueError with message "incorrect login 'abc'".
# Note that all data may be case-insensitive.
import re


def check(login):
    pattern = r"^(admin|employee)(-id|-|id)?\d+$"
    try:
        if not re.match(pattern, login, re.IGNORECASE):
            raise ValueError(f"incorrect login '{login}'")
        return True
    except ValueError as e:
        raise e

correct_login = "employee-124"
print(check(correct_login)) #True

incorrect_login = "incorrect_login"
try:
    print(check(incorrect_login))
except ValueError:
    print("Catched") #Catched