
import math

# n = a^3 + b^3 + c3

def find_integer_solutions(n):
	a = None
	b = None
	c = None

	for i in range(0,1001):
		if math.pow(i, 3) == n:
			a = i
			b = 0
			c = 0
		elif math.pow(i, 3) == n/2.0:
			a = i
			b = i
			c = 0
		elif math.pow(i, 3) == n/3.0:
			a = i
			b = i
			c = i

	return [a, b, c]

