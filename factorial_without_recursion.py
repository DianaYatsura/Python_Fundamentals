"""Task3. Write a script that will calculate the factorial of the entered number without using recursion.
Example: 0!=1, 1!=1, 2!=1*2, 3!= 1*2*3=6"""
import math
from math import factorial

def factorial_n(num):
    if num == 0:
        return 1
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

num = int(input ('Enter a number '))
print (f'{num}! = {factorial(num)}')

# OR another version
for n in input("Enter a number "):
    print(f'{n}! = {math.factorial(int(n))}')
