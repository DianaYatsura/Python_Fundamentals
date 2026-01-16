"""In the range from 1 to 10 determine:
• even numbers that are divisible by 2,
• odd numbers, which are divisible by 3,
• numbers that are not divisible by 2 and 3"""

even_numbers, odd_numbers, not_divisible_by_2_3  = [], [], []

for num in range(1,10):
    if num % 2 == 0:
        even_numbers.append(num)
    elif num % 3 == 0:
        odd_numbers.append(num)
    else:
        not_divisible_by_2_3.append(num)

print(f"Even: {even_numbers} \nOdd: {odd_numbers} \nNot_divisible: {not_divisible_by_2_3} ")
