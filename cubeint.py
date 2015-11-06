
import math

# n = a^3 + b^3 + c3

def find_integer_solutions(n):
	a = 0
	b = 0
	for i in range(0,100):
		if math.pow(i, 3) == n:
			a = i
		elif math.pow(i, 3) == n/2:
			a = i
			b = i

	return [a, b, 0]








