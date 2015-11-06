
from cubeint import find_integer_solutions
import math


def check_equality_order_independent(expected, actual):
	product_expected = 0
	product_expected += math.pow(int(expected[0]), 3)
	product_expected += math.pow(int(expected[1]), 3)
	product_expected += math.pow(int(expected[2]), 3)

	product_actual = 0
	product_actual += math.pow(int(actual[0]), 3)
	product_actual += math.pow(int(actual[1]), 3)
	product_actual += math.pow(int(actual[2]), 3)

	return product_expected == product_actual

def assertSolution(n, expected, debug=True):
	actual = find_integer_solutions(n)

	if debug:
		print('f(' + str(n) + ') = ' + str(actual))
	
	if not check_equality_order_independent(expected, actual):
		print('FAIL')
		print('n = ' + str(n))
		print('expected: ' + str(expected))
		print('actual: ' + str(actual))
		print('')

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

assertSolution(-1, [0, 0, 0])
assertSolution(4,  [0, 0, 0])
assertSolution(5,  [0, 0, 0])
assertSolution(13, [0, 0, 0])
assertSolution(14, [0, 0, 0])
assertSolution(22, [0, 0, 0])
assertSolution(23, [0, 0, 0])
assertSolution(31, [0, 0, 0])
assertSolution(32, [0, 0, 0])



'''
#known cubes
assertSolution(0, [0,0,0])
assertSolution(1, [1,0,0])
assertSolution(8, [2,0,0])
assertSolution(970299, [99,0,0])

#double a cubed number
assertSolution(2, [1, 1, 0])
assertSolution(16, [2, 2, 0])
assertSolution(54, [3, 3, 0])
assertSolution(128, [4, 4, 0])
assertSolution(1940598, [99,99,0])

#triple a cubed number
assertSolution(3, [1, 1, 1])
assertSolution(24, [2, 2, 2])
assertSolution(81, [3, 3, 3])
assertSolution(2910897, [99, 99, 99])
assertSolution(3 * math.pow(10,9), [1000, 1000, 1000])
assertSolution(3 * math.pow(10,9) + 1, [None, None, None])
'''
