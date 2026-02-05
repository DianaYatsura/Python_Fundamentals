"""Write a program that prompts the user to enter their age, and then displays a message
stating whether the age is even or odd. The program must provide the ability to enter
a negative number, and in this case generate an exception. The master code should call
a function that processes the information entered."""


class MyError(Exception):
    def __init__(self, message="Negative number error"):
        super().__init__(message)


def check_age(age):
    try:
        age = int(age)

        if age <= 0:
            raise MyError(f"Your input contains inappropriate number: {age}. Try again.")

        return check_odd_even(age)

    except ValueError:
        return "You entered not a number."
    except MyError as e:
        return str(e)


def check_odd_even(age):
    return f"Your age {age} is even" if age % 2 == 0 else f"Your age {age} is odd"


age = input("Enter your age: ")
print(check_age(age))
