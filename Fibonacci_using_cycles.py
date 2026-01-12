"""Print Fibonacci numbers up to the entered number n, using cycles.
(Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)"""

def fibonacci_numbers(number):
    i = 0
    c = 1
    while i <= number:
        print(i, end=' ')
        i, c = c, i + c

fibonacci_numbers(int(input('Enter a number ')))