# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

import string

def pig_it(text):
    my_list = text.split()
    final = []
    for item in my_list:
        if item not in string.punctuation:
            #print(f"alpha : {item}")
            
            #take the first letter, remove it from that position of the word
            #and then add it to the end of the word together with "ay"
            first_let = item[0]
            new_string = item[1:]
            new_string += first_let + "ay"
            #print(new_string)
            
            final.append(new_string)
            
        else: 
            final.append(item)
    
    final_final = " ".join(final)    
    print(final_final)
    return " ".join(final)