# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.

import string

def alphabet_position(text):
    final = []
    for letter in text.lower():
        if letter.isalpha():
            pos = ord(letter) - ord('a') + 1
            final.append(str(pos))
            
        else: pass
    
    return " ".join(final)