'''Write a function that takes a credit card number and only displays the last four characters.
The rest of the card number must be replaced by ************
If the length of the number is less than 16 symbols the function returns "Invalid card"'''

def card_hide(card):
    if len(card) < 16:
        print ("Invalid card")
    elif len(str(card)) == 16:
        print (f'{card.replace(card[0:12],"************")}')

# input cards values for checking
card_hide(card=)