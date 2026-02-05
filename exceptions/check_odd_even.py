'''Write the function check_odd_even (number) whose input parameter is an integer number. The function checks
whether the set number is even or odd:
in the case of an even number the function should be displayed the corresponding message - "Entered number is even";
in the case of an odd number the function should be displayed the corresponding message - "Entered number is odd";
in the case of incorrect data the function should be displayed the message - "You entered not a number.'''

def check_odd_even(number):
    try:
        if int(number) % 2 == 0:
            return "Entered number is even"
        elif int(number) % 2 == 1:
            return "Entered number is odd"
    except (NameError, ValueError):
        return "You entered not a number"

