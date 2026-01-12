"""
Create a list that contains elements of integer type, then use
the loop to change the type of these elements to a floating type.
(Hint: use the built-in float () function).
"""
# enter your values in list for checking
some_list = [1, 'text', 4, 'message', 5, 3, 6, 7, 9]

for i, n in enumerate(some_list):
    if type(n) is int:
        some_list[i] = float(n)
print(some_list)
