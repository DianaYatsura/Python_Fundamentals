"""Create a function that takes a list and finds the list of integers that appear
an odd number of times. """

def find_odd(lst):
    new_list = []
    for el in lst:
        if lst.count(el) % 2 == 1 and el not in new_list:
            new_list.append(el)
    return new_list


print(find_odd([20, 1, 1, 2, 1, 2, 3, 3, 5, 5, 4, 20, 4, 5]))   # [1, 5]
print(find_odd([10]))                                           # [10]
print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))           # [-1]