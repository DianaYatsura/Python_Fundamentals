
number = input("Please, input a four-digit natural number ")


product_of_digits = 1
for d in number:
    product_of_digits *= int(d)

print(f'The product of the digits of {number} is {product_of_digits}')


reversed_number = ''.join(reversed(number))
print(reversed_number)


sorted_number = ''.join(sorted(number))
print(sorted_number)