# Slicing and math practice
# The slice object initialization takes in 3 arguments with the last one being the optional index increment. The general method format is: slice(start, stop, increment), and it is analogous to start:stop:increment when applied to a list or tuple.

def conv_baseX_baseTEN(base, num):
    base = int(base)
    # add each digit as single string character in list
    num = [int(x) for x in str(num)]
    # reverse list order for easier operation
    num = num[::-1]
    result = 0
    # recursively add the result of c(x**i)
    # beginning with first digit of input number, c = digit value
    # satisfies arithmetic series formula:
    # as n -> infinity, where n is number of digits for a given integer, 
    # and c is the coefficient of each digit, and i represents the ordinal 
    # position of each digit starting from the least significant digit,
    # and x is the base number of the counting system
    # sum { c(x**(i)) + ... + c(x**2) + c(x**1) + c(x**0) }
    for i in range(len(num)):
        result += int(num[i])*(base**i)

    return result

# print convbaseten(3,1212)

hexlist = []

def conv_baseTEN_baseX(base, num)



"""    
# This is way to fucking complicated to even bother with, 
# but I'll leave it here as a stern reminder for myself
for i in range(len(num)):
#        addingMatrix = []
        j = (-1*i)-1    
        l = a**i
        if i == 0:
            k = None
        else:
            k = -1*i
        m = 
#        print b[j:k:]
#        print len(b[j:k:])
#        addingMatrix.append(int(b))
        x =
        print "\n %s x %s = x" %(str(l),b[j:k], x)"""

#    print addingMatrix
#   print li"""
# converts from base 10 to any other base number