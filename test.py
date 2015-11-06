
from cubeint import find_integer_solutions
import math

def assertSolution(n, expected):
	actual = find_integer_solutions(n)

	errorstring = ''
	errorstring += '\nexpected: ' + str(expected)
	errorstring += '\nactual: ' + str(actual)

	assert actual == expected, errorstring

#assertSolution(n, [a, b, c])

assertSolution(0, [0,0,0])
assertSolution(1, [1,0,0])
assertSolution(8, [2,0,0])
assertSolution(970299, [99,0,0])

assertSolution(2, [1, 1, 0])
assertSolution(16, [2, 2, 0])
assertSolution(1940598, [99,99,0])

assertSolution(3, [1, 1, 1])
assertSolution(24, [2, 2, 2])
assertSolution(81, [3, 3, 3])
assertSolution(2910897, [99, 99, 99])
assertSolution(3 * math.pow(10,9), [1000, 1000, 1000])
assertSolution(3 * math.pow(10,9) + 1, [None, None, None])

assertSolution(-1, [None, None, None])
assertSolution(25, [None, None, None])
assertSolution(26, [None, None, None])

