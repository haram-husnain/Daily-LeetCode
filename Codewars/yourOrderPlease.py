def order(sentence):
    if not sentence:
        return ""
    result = []
    split_up = sentence.split()
    
    for i in range(1,10): #1 until 10
        for item in split_up: #each word in the split list
            if str(i) in item: # if the number from the range is in the word or the item
                result.append(item) #add the item
                
                #since looping through the range before the words, meaning the appending is based off the range
                
                # so if the number is not in the word, it wont be appended at that position in the result
                # it will be skipped to the next item in the split
    
    #return " ".join(result)
    final = " ".join(result)
    print(final)

sample = "not3 tes5t is2 a4 this1"
order(sample)

# Your task is to sort a given string. Each word in the string will contain a single number. 
# This number is the position the word should have in the result. 
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0). If the input string is empty, return an empty string. 
# The words in the input String will only contain valid consecutive numbers.