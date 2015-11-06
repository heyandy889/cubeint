
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

def assertSolution(n, expected):
	actual = find_integer_solutions(n)

	errorstring = ''
	errorstring += '\nexpected: ' + str(expected)
	errorstring += '\nactual: ' + str(actual)

	assert actual ==expected, errorstring

#assertSolution(n, [a, b, c])
assertSolution(0, [0,0,0])
assertSolution(1, [1,0,0])
assertSolution(8, [2,0,0])
assertSolution(970299, [99,0,0])

assertSolution(2, [1, 1, 0])
assertSolution(16, [2, 2, 0])
assertSolution(1940598, [99,99,0])







