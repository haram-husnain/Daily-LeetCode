def build_matrix(rows, cols):
    # a = [[0 for _ in range(cols)] for _ in range(rows)]
    # print(a)
    return [[0 for _ in range(cols)] for _ in range(rows)]

build_matrix(2, 3)

# Given two integers (a number of rows and a number of columns), return a matrix (an array of arrays) filled with zeros (0) of the given size.