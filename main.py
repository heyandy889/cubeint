

from cubeint import find_integer_solutions


print('')
print('n^3 = a^3 + b^3 + c^3')
print('')

print('n' + ': ' + '[a, b, c]')
for n in range(31):
	result = find_integer_solutions(n)
	print(str(n) + ': ' + str(result))

