# remove everything inside the parentheses as well as the parentheses themselves.
def remove_parentheses(st):
    result = []
    depth = 0

    for char in st:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        elif depth == 0:
            result.append(char)
    return ''.join(result)

# import re
# def remove_parentheses(st):
#     return re.sub('/([^.()]*/)', '', st)

mine = remove_parentheses('a(b)')
ans = 'a'

print(mine == ans)

