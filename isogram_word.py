""" An isogram is a word that has no duplicate letters. Create a function that takes a string
and returns either True or False depending on whether or not it's an "isogram".
Notes.
*** ignore letter case (should not be case sensitive).
*** test cases contain valid one word strings."""

def is_isogram(word):
    chars = set(word.lower())
    return len(chars) == len(word)


print(is_isogram("Algorism")) # True
print(is_isogram("PasSword")) # False
print(is_isogram("Consecutive")) # False