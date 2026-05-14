# Implement a function that computes the difference between two lists. The function should remove all occurrences of elements from the first list (a) that are present in the second list (b). The order of elements in the first list should be preserved in the result.

def array_diff(a, b):
    for item in (a+b):
        if item in a and item in b:
            a.remove(item)
    print(a)
    
array_diff([],[1,2])