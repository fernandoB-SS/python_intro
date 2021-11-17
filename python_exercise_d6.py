import numpy

# array of ten zeros
# array_zeros = numpy.zeros((2, 5), dtype=int)
array_zeros = numpy.zeros((10), dtype=int)

# 3. Create an array of 10 ones
# array_ones = numpy.ones((2,5), dtype=int)
array_ones = numpy.ones((10), dtype=int)

# 4. Create an array of 10 fives
# array_fives = numpy.ones((2, 5), dtype=int) * 5
array_fives = numpy.ones((10), dtype=int) * 5

# 5. Create an array of integers from 10 to 50
# end step is exclusive
array_integers = numpy.arange(10, 51)

# 6. Create an array of even integers from 10 to 50
# func( start: end : step)
array_even_integers = numpy.arange(10, 51, 2)

# 7. Create a 3x3 matrix with values ranging from 0 to 8
user_matrix = numpy.arange(9).reshape(3, 3)

# 8. Create a 3x3 identity matrix
user_identity_matrix = numpy.eye((3), dtype=int)
# 9. Use numpy to randomly generate a number between 0 and 1
random_number = numpy.random.rand(1)

print(f"Array of Zeros{array_zeros}")
print(f"Array of Ones: \n{array_ones}")
print(f"Array of Fives: \n{array_fives}")
print(f"Array of Integer: \n{array_integers}")
print(f"Even Array: \n{array_even_integers}")
print(f"3x3 Matrix: \n{user_matrix}")
print(f"Identity Matrix: \n{user_identity_matrix}")
print(f"Random Number: \n{random_number}")
