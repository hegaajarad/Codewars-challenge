# Write a function that takes an integer as input, 
# and returns the number of bits that are equal to one 
# in the binary representation of that number. 
# You can guarantee that input is non-negative.
# 
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case


def countBits(n):
    bits = "{0:b}".format(n) # I used ("{0:b}".format(n)) to convert an intger input to binary
    myBits = bits.count('1')
    return myBits



print(countBits(0))
print(countBits(4))
print(countBits(7))
print(countBits(9))
print(countBits(10))
