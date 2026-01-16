'''Counting the number of digits in the whole number, including:
For example:
count_digits(123) == 3
count_digits(-23) == 2
count_digits(3)==1
Also please check if the data type is number, whether its not please print a message "Wrong data type"'''


def count_digits(number):
    if isinstance(number, (int,float)) :
        print(len(str(abs(number))))
    else:
        print("Wrong data type")


#enter number for checking
count_digits(number=)
