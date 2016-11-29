#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#
# Note: Most of the main method has been copy pasted from t7e1.py, and therefore was not commented again
#

def main():
	my_list = []

	print("Your list is currently", my_list)

	num_values = int(input("How many values will you enter? "))

	for i in range(num_values):
		my_list.append(-1)

	for i in range(num_values):
		print("Your list is currently", my_list)
		print("What value should replace the element at index ", i, "? ", sep="", end="")
		replace_with = int(input())
		my_list[i] = replace_with

	print("Your final list is", my_list)
	print("The sum of the elements in the list is:", list_sum(my_list))

# Returns the sum of the elements in the list.
# If any of the elements in the list are not numbers, returns 0.
def list_sum(x):
	# Calculate and return the sum, if every element is a number
	if every_element_is_number(x):
		sum = 0
		for i in range(len(x)):
			sum += x[i]
		return sum
	# Otherwise, return 0
	else:
		return 0

# Determine if every element in a list is a number
# Return True if every element is a number; otherwise return False
def every_element_is_number(x):
	for i in range(len(x)):
		if type(x[i]) != int:
			return False
	return True

# Entrypoint of program
main()