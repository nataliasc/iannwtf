'''
Define a list with squares of all numbers from 0 to 100 in just one line.
Bonus: Only include those squares that are divisible by 2, but still keep it in one line.
'''
squares = [x**2 for x in range(101) if (x**2) % 2 == 0]
print(squares)




