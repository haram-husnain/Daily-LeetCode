def move_zeros(lst):
    write_index = 0
    
    for i in lst:
        if i != 0:
            lst[write_index] = i
            write_index += 1
    
    total_zeros = len(lst) - write_index
    lst[write_index:] = [0] * total_zeros
    
    return lst

#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
#move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
