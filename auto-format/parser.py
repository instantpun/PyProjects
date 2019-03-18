# practice argparse

import argparse

# show nth fibonacci number

def fib(n):
	a, b = 0, 1
	for it in range(n):
		a, b = b, a+b
		print(str(a))
	return a

def Main():
	parser = argparse.ArgumentParser(description='do some stuff')
	parser.add_argument("num", help='The fibonacci number you wish to calculate', type=int)

	args = parser.parse_args()

	result = fib(args.num)
	print("The " + str(args.num) + "th fib number is " + str(result))

if __name__ == '__main__':
	Main()


