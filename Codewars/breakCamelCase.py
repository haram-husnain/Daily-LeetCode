# Complete the solution so that the function will break up camel casing, using a space between words.
# if uppercase letter in word not first, add space

def solution(s):
    s2 = []
    for c in s:
        if c.isalpha():
            if c != s[0] and c.isupper():
                c = " " + c
                
            s2.append(c)
                
                
        else: pass
    
    final = "".join(s2)
    print(final)

solution("breakCamelCase")