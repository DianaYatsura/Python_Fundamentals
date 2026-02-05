#Write your code bellow to create custom Error named InputError and function check.
#The error must save description of error in data attribute.
#In data of error must be written:
#"Short text error" if length of string less than 3,
#"Long text error" if length of string more than 15,
#"Type text error" if we try to check not string.
#Your function check will be called from function test_input

class InputError(Exception):

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def check(text):
    try:
        if type(text) != str:
            return "Type text error"
        elif len(text) > 15:
            return "Long text error"
        elif len(text) < 3:
            return "Short text error"
    except InputError as e:
        print(e.data)
    else:
        return True


def test_input(text):
    try:
        print(check(text))
    except InputError as e:
        print(e.data)

test_input("") #Short text error
test_input("Hello world") #True
test_input("Long text that can not be placed in some document") #Long text error
test_input({}) #Type text error