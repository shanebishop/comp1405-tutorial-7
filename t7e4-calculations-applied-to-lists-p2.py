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
	print("The sum of even elements is:", sum_of_even(my_list))
	print("The sum of odd elements is: ", sum_of_odd(my_list))
	print("Here are all the non-numeric elements: ", end="")
	if len(concat_nonnumeric_elements(my_list)) == 0:
		print("There are no non-numeric elements.")
	else:
		print(concat_nonnumeric_elements(my_list))

# Calculate the sum of all of the even numbers in the list
def sum_of_even(x):
	sum = 0
	for i in range(len(x)):
		if type(x[i]) == int or type(x[i]) == float:
			if x[i] % 2 == 0:
				sum += x[i]
	return sum

# Calculate the sum of all of the odd numbers in the list
def sum_of_odd(x):
	sum = 0
	for i in range(len(x)):
		if type(x[i]) == int or type(x[i]) == float:
			if x[i] % 2 != 0:
				sum += x[i]
	return sum

# Concatenate all of the non-numeric elements of the list
def concat_nonnumeric_elements(x):
	growing_string = ""
	for i in range (len(x)):
		if type(x[i]) != int:
			growing_string += x[i]
	return growing_string

# Entrypoint of the program
main()