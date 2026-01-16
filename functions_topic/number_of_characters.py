"""Write a function that calculates the number of characters included in a given string
• input: "hello"
• output: {"h":1, "e":1,"l":2,"o":1} """

def number_of_characters(word):
    output = {}
    for w in word:
        output[w] = word.count(w)
    return output

print(number_of_characters(word='hello'))   # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(number_of_characters(word='documentation')) # {'d': 1, 'o': 2, 'c': 1, 'u': 1, 'm': 1, 'e': 1, 'n': 2, 't': 2, 'a': 1, 'i': 1}