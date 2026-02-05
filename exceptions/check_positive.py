#Write the function check_positive(number)whose input parameter is a number.
# The function checks whether the set number is positive or negative:
#in the case of a positive number the function should be displayed the corresponding message
# - "You input positive number: input parameter of function"
#in the case of a negative parameter the function should return the exception
# of your own class MyError and displayed the corresponding message.
# "You input negative number: input parameter of function. Try again."
#in the case of incorrect data the function should be displayed the message - "Error type: ValueError!"

class MyError(Exception):
    def __init__(self, message ):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


def check_positive(number):
    try:
        num = float(number)
        if num < 0:
            raise MyError(f'You input negative number: {num}. Try again.')
    except (ValueError, TypeError):
        return "Error type: ValueError!"
    except MyError as me :
        return me
    else:
        return f'You input positive number: {num}'


print(check_positive(8.9)) #You input positive number: 8.9
print(check_positive("45")) #You input positive number: 45.0
print(check_positive(-19)) #You input negative number: -19.0. Try again.
print(check_positive("abs")) #Error type: ValueError!
print(isinstance(check_positive("-235"), MyError)) #True




