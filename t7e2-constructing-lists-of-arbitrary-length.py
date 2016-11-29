#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

# Initializes an empty list
my_list = []

# Determines if the while loop (below) should continue to iterate
keep_going = True

# Main loop
while keep_going:
	# Prints the current list
	print("Your list is currently", my_list)
	
	# Asks the user what they want to do next
	command = input("Would you list to (a)dd a value, (r)emove the last value, or e(x)it? ").upper()
	
	# If the user wants to add an element, retrieve their input and add it to the list
	if command == "A":
		to_add = int(input("What value would you like to add? "))
		my_list.append(to_add)
	# Removes the last element
	elif command == "R":
		my_list.pop()
	# The user has quit the program
	else:
		print("Goodbye")
		keep_going = False