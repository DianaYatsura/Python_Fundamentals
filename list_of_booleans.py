"""Create a function which returns a list of booleans, from a given number. Iterating through
the number one digit at a time, append True if the digit is 1 and False if it is 0.
Notes. Expect numbers with 0 and 1 only. """


def integer_boolean(binary_number):
    list_of_booleans = []
    for d in binary_number:
        if d == '1':
            list_of_booleans.append(True)
        else:
            list_of_booleans.append(False)
    return list_of_booleans

print(integer_boolean("100101")) # [True, False, False, True, False, True]
print(integer_boolean("10")) # [True, False]
print(integer_boolean("001")) # [False, False, True]