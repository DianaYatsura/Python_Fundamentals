"""Write a program that calculates the area of a rectangle, triangle and circle
(write three functions to calculate the area, and call them in the
main program depending on the user's choice)"""

def area_choice():
    shape = input("Please, choose and enter a shape: rectangle, triangle or circle ")
    if shape == 'rectangle':
        def area_of_rectangle():
            w, l = int(input('enter a width ')), int(input('enter a length '))
            result = w * l
            return round(result, 2)
        print(f'The area of rectangle is: {area_of_rectangle()}')
    elif shape == 'triangle':
        def area_of_triangle():
            b, h = int(input('Enter a base ')), int(input('Enter a height '))
            result = 1 / 2 * b * h
            return round(result, 2)
        print(f'The area of triangle is: {area_of_triangle()}')
    elif shape == 'circle':
        def area_of_circle():
            PI = 3.14
            r = int(input('Enter a radius '))
            result = PI * r ** 2
            return round(result, 2)
        print(f'The area of circle is: {area_of_circle()}')


area_choice()