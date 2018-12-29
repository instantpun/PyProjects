# this is some basic practice with the slice() method
li = ['1','2','3','4','5']
print li
print li[::-1]

a = "123456"

# starts at position 0 and increment the pointer/index -1
# in essence, it processes the list backwards, one position at a time
# this allows us to reverse the list
print a[::-1]
print a[::-2]
# slice evaluates arithmetic before processing the elements
i = 3
print a[(i-1):4]
# takes last character in string
print a[-1:]
# returns last character, and increments by two positions from end of string towards start
print a[-1::-2]
# returns all characters minus last one
print a[:-1]

# converts from any other base number to base 10
# a = base, b = number

# this reverses the order of a list
# sliceObj = slice(0::-1) 