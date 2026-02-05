"""Write a program that analyzes the entered number and, depending on the number, gives the day
of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take into account
cases of entering numbers from 8 and more, as well as cases of entering non-numerical data."""

def day_of_week(number):

    week = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }
    try:
        number = int(number)
        if  number < 1 or number > 7:
            return 'The number must be between 1 and 7.'
        return f'{number} is {week[number]}'
    except ValueError:
        return "You entered an invalid value. Please, enter a number."


number = input("Enter a number ")
print(day_of_week(number))