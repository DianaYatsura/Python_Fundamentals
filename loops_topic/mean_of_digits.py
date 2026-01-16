"""Create a function that returns the mean of all digits.
The mean of all digits is the sum of digits / how many digits there are
(e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=3).
The mean will always be an integer. """

def mean(number):
    digits = []
    for n in str(number):
        digits.append(int(n))
    return round(sum(digits)/len(digits))

# input value for number for checking
print(mean(number=))