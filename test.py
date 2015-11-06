
from cubeint import find_integer_solutions
import math

def assertSolution(n, expected):
	actual = find_integer_solutions(n)

	errorstring = ''
	errorstring += '\nexpected: ' + str(expected)
	errorstring += '\nactual: ' + str(actual)

	assert actual == expected, errorstring

#assertSolution(n, [a, b, c])

#known cubes
assertSolution(0, [0,0,0])
assertSolution(1, [1,0,0])
assertSolution(8, [2,0,0])
assertSolution(970299, [99,0,0])

#double a cubed number
assertSolution(2, [1, 1, 0])
assertSolution(16, [2, 2, 0])
assertSolution(1940598, [99,99,0])

#triple a cubed number
assertSolution(3, [1, 1, 1])
assertSolution(24, [2, 2, 2])
assertSolution(81, [3, 3, 3])
assertSolution(2910897, [99, 99, 99])
assertSolution(3 * math.pow(10,9), [1000, 1000, 1000])
assertSolution(3 * math.pow(10,9) + 1, [None, None, None])

#known cases with no solution
assertSolution(-1, [None, None, None])
assertSolution(4, [None, None, None])
assertSolution(5, [None, None, None])
assertSolution(13, [None, None, None])
assertSolution(14, [None, None, None])
assertSolution(22, [None, None, None])
assertSolution(23, [None, None, None])
assertSolution(31, [None, None, None])
assertSolution(32, [None, None, None])

#just working through simple cases
assertSolution(0, [0, 0, 0])

assertSolution(1, [1, 0, 0])
assertSolution(2, [1, 1, 0])
assertSolution(3, [1, 1, 1])

assertSolution(8, [2, 0, 0])
assertSolution(9, [2, 1, 0])
assertSolution(10, [2, 1, 1])
assertSolution(16, [2, 2, 0])
assertSolution(17, [2, 2, 1])
assertSolution(24, [2, 2, 2])

assertSolution(27, [3, 0, 0])
assertSolution(28, [3, 1, 0])
assertSolution(29, [3, 1, 1])
assertSolution(35, [3, 2, 0])
assertSolution(36, [3, 2, 1])
assertSolution(43, [3, 2, 2])
assertSolution(54, [3, 3, 0])
assertSolution(55, [3, 3, 1])
assertSolution(62, [3, 3, 2])
assertSolution(81, [3, 3, 3])

