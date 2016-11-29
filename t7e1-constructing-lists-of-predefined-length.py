#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

# Initializes an empty list
my_list = []

# Prints the current list
print("Your list is currently", my_list)

# Asks the user for a number of values to add to the list
num_values = int(input("How many values will you enter? "))

# Makes every value in the list -1
for i in range(num_values):
	my_list.append(-1)

# Iterates through the list, allowing the user to change each element as the program comes to it
for i in range(num_values):
	print("Your list is currently", my_list)
	print("What value should replace the element at index ", i, "? ", sep="", end="")
	replace_with = int(input())
	my_list[i] = replace_with

# Prints the final list and thanks the user for using the program
print("Your final list is", my_list)
print("Thank-you for using this program.")