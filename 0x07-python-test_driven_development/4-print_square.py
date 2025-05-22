#!/usr/bin/python3

"""A module for printing a square"""


def print_square(size):
	"""A function that prints the size of a square
	Args:
		size(int): the size of the square to be printed
	Raises:
		TypeError: if size is not an integer
		ValueError: if size is < 0
	"""

	if type(size) is not int:
		raise TypeError("size must be an integer")
	if size < 0:
	 	raise ValueError("size must be >= 0")
	for i in range(size):
		print("#" * size)
