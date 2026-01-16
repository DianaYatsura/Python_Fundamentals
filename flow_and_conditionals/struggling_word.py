"""Write a function that stutters a word as if someone is struggling to read it.
The first two letters are repeated twice with an ellipsis ... , and then the word
is pronounced with a question mark ?.
If the input is less than two characters long, the function prints "oh..."."""

def stutter(word):
    if len(word) < 2:
        print("oh...")
    else:
        print((word[0:2] + '...')*2 + (word +'?'))

#input the word for checking
stutter(word=)
