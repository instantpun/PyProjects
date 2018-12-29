# this populates the list with zeroes
# inserts value 0 at each coordinate inside li[x][y]
# specifically value 0 is inserted in both subset 0 and subset 1 within the array
# and this value is generated again for both subsets at index 0 thru 9
li = [[0] * 3 for a in range(10)]
# this replaces the default value of each coordinate within list named li
# number of lists, x, each with y number values
for x in range(10):
    for y in range(3):
        if y == 0:
            li[x][y]=x
        elif y == 1:
            li[x][y]=x**3
        elif y == 2:
            z = x**3
            #converts z to str, grabs the last digit, and conv back to int
            li[x][y]=int(repr(z)[-1])
        # else statement here keeps values at zero, in case of bad input later.
        else:
            li[x][y]=0
        # print(li[x][y])
        # print(li[x][1])
#print(li)

def tensdigit(a):
    # conv input into 6 digit str with leading zero
    a = str(format(a, '06'))
    #print a
    # slices digits from index 0 up to but not including 3, and conv back to int
    a = int(a[0:3])
    #print a
    for x in range(10):
        # if state is false, continue loop
        if not li[x][1] <= a < li[x+1][1]:
            continue
        # returns the first instance of x, that is true
        else:
            return x

def onesdigit(a):
    a = int(repr(userInput)[-1])
    for x in range(10):
        if not a == li[x][2]:
            continue
        else:
            return li[x][0]

def solve(a):
    if len(str(a)) > 6 or len(str(a)) < 4:
        print("{0} is invalid input".format(a))
    else:
        ans = str(tensdigit(a))+str(onesdigit(a))
        print(ans)

userInput = 216000
solve(userInput)

"""    while li[x][1] <= a < li[x+1][1] is false:
    	x += 1
    	return x"""

""" def cuberoot(x)
	for x in range(10)
    	if int(repr(userInput)[-1]) = li[x][2] and :
        	onesDigit = li[x][0]


    	return onesDigit """




# for i in range(0,10):
#	for j in range(0,3):
#    	print li[i][j]


# this forces any integer to have three digits with leading zeroes
# print('{:03}'.format(1))

#	for b in range(a):
#    	sample[a][b].append(a*a*a)
#for x in range(10, 100):
#	y = x*x*x
#	print("base %s, cube of base %s" %(x,y))
