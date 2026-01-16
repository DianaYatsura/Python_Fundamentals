import this, codecs
from idlelib.replace import replace

zen_str = codecs.decode(this.s, "rot13")


print('***  Number of occurrences of the words:  ***'
    f'\n {zen_str.count("better")} --> better'
    f'\n {zen_str.count("never")} --> never'
    f'\n {zen_str.count("is")} --> is')

print('*** ', zen_str.upper())

print('*** ', zen_str.replace('i', '&'))