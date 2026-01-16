""" Write a function taking in a string like 'WOW this is REALLY          amazing'
and returning Wow this is really amazing. String should be capitalized and properly spaced."""

def filter_words(st):
    st = " ".join(st.capitalize().split())
    return st

#enter string for checking
print(filter_words(st=""))