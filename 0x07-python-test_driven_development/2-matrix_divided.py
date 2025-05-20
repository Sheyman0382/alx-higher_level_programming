#!/usr/bin/python3

"""A module that divides all elements of a matrix by a given number"""


def matrix_divided(matrix, div):
	"""
	Divides all elements of all matrix by a given divisor
	Args:
		matrix (list of lists): the matrix to be divided
		div (int or float): the number to divide each element by
	Returns:
		list of lists of int or float: A new matrix with the results of the division, rounded to 2 decimal places.
	Raises:
		TypeError: if matrix isn't a list of int/float
				or if all rows in matrix do not have the same size
				or if div is not an integer or a float
	ZeroDivisionError: If div is zero
	"""
	
	if not isinstance(div, (int, float)):
		raise TypeError ("div must be a number")
	if div == 0:
	 	raise ZeroDivisionError ("division by zero")
	if not isinstance(matrix, list):
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

	row_length = matrix[0]

	for row in matrix:
		if not isinstance(row, list):
			raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
		if len(row) != row_length):
			raise TypeError("Each row of the matrix must have the same size")
        for element in row:
			if not isinstance(element, (int, float)):
				raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
	
	new_matrix = []
	for row in new_matrix:
		new_row = []
		for element in row:
			result = round(element / div, 2)
			new_row.append(result)
		new_matrix.append(new_row)
	return new_matrix
