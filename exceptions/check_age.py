#With help input obtain from user his age. Age must be natural number.
#If user try input incorrect value ask him again. If user typed correct age print this value.
#Do not use if in your code, but you can use already created function check_age for validation.

def check_age(age):
    try:
        while int(age) <= 0:
            age = input()
        print(int(age))
        return int(age)
    except ValueError:
        return check_age(input())

age = check_age(input())