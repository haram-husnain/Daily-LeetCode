#2 strings alpha only, a new string adds them together
#sort them alphabetically and remove repeating and return the longest

#set is going to remove duplicaes, its then sorted in a list by defuslt and then joined together in alpha_sort
def longest(a1, a2):
    
    # if letters in a1 and a2 are alpha
    a3 = a1 + a2
    
    if a3.isalpha(): 
        
        alpha_sort = ''.join(sorted(set(a3)))
        print(alpha_sort)
        #return a3

    else: return None
    
longest("loopingisfunbutdangerous", "lessdangerousthancoding")

# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string (alphabetical ascending), 
# the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.