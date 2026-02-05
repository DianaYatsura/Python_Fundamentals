# Write the function divide(numerator, denominator) the two input parameters of which are numbers. The function returns the result of dividing two numbers.
# in case of correct data the function should be displayed the corresponding message – "Result is numerator / denominator"
# in the case of division by zero the function should be displayed the corresponding message – "Oops, numerator / denominator, division by zero is error!!!".
# in the case of incorrect data the function should be displayed the message –"Value Error! You did not enter a number!"

def divide(numerator, denominator):
    try:
        if not isinstance(numerator, int or float) or not isinstance(denominator, int or float):
            raise TypeError
        if denominator == 0:
            return f"Oops, {numerator}/{denominator}, division by zero is error!!!"
        return f"Result is {numerator/denominator}"
    except TypeError:
        return "Value Error! You did not enter a number!"

print(divide(4, 8)) #Result is 0.5
print(divide(8, 0)) #Oops, 8/0, division by zero is error!!!
print(divide(-1, 4)) #Result is -0.25
print(divide("9", 3)) #Value Error! You did not enter a number!