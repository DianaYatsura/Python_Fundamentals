""" Given a list of numbers, create a function which returns the list but with each element's index
in the list added to itself. This means you add 0 to the number at index 0, add 1 to the number
at index 1, etc"""


def add_indexes(lst):
    result = []
    for el, num in enumerate(lst):
        result.append(el + num)
    return result


print(add_indexes([0, 0, 0, 0, 0]))    # [0, 1, 2, 3, 4]
print(add_indexes([1, 2, 3, 4, 5]))    # [1, 3, 5, 7, 9]
print(add_indexes([0, -1, -2, -3, -4])) # [0, 0, 0, 0, 0]