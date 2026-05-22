def zip_strings(a, b):
    result = ""
    length = min(len(a), len(b))
    for i in range(length):
        result += a[i] + b[i]

    return result + (a[length:] + b[length:])

#1st string starts the new string
#remaining chars will go in the end
#nested for loops?
