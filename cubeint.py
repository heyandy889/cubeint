
import math

# n = a^3 + b^3 + c3

def find_integer_solutions(n):
	a = 0
	b = 0
	c = 0

	while math.pow(a, 3) < n:
		a += 1

	if math.pow(a, 3) > n:
		a -= 1

	while math.pow(b, 3) < (n-math.pow(a,3)):
		b += 1

	if math.pow(b, 3) > (n-math.pow(a,3)):
		b -= 1

	while math.pow(c, 3) < (n-math.pow(a,3)-math.pow(b,3)):
		c += 1

	if math.pow(c, 3) > (n-math.pow(a,3)-math.pow(b,3)):
		print 'uh oh'

	return [a, b, c]



















