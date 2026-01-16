""" You need to write a function that reverses the words in a given string.
Words are always separated by a single space.
As the input may have trailing spaces, you will also need to ignore unnecessary whitespace."""

def reverse(st):
    words = st.strip().split()
    return ' '.join(reversed(words))


print(reverse('Hello World'))  # World Hello
print(reverse('Hi There.'))    # There. Hi