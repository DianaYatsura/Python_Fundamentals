"""Create a function that takes a string and returns the number (count) of vowels contained within it.
Notes
* a, e, i, o, u are considered vowels (not y).
* test cases are one word and only contain letters"""

def count_vowels(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    result = 0
    for v in word:
        if v in vowels:
            result +=1
    return result

#input a word for checking
print(count_vowels(word=''))
