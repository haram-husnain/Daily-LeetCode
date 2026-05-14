#Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

#Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
    
def count_bits(n):
    
    bin_conv = list(bin(int(n))[2:])
    print(bin_conv)
    fin=0
    for i in range(len(bin_conv)):
        fin +=  int(bin_conv[i])
        i+=1
    print(fin)
    
    return fin

count_bits(1234)
    