
import math

# n = a^3 + b^3 + c3

def cubes(a, b, c):
	return math.pow(a,3) + math.pow(b,3) + math.pow(c,3)

def find_integer_solutions(n):
	a = 0
	b = 0
	c = 0

	while n > cubes(a,b,c):
		a += 1

		while n > cubes(a,b,c):
			b += 1

		if n < cubes(a,b,c):
			b -= 1

		while n > cubes(a,b,c):
			c += 1

		if n < cubes(a,b,c):
			b = 0
			c = 0

	if n != cubes(a,b,c):
		return [0, 0, 0]

	return [a, b, c]










