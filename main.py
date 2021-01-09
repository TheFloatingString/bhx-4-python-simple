# code for BrebeufHx 4 Python workshop 
# all lines of code with a "#" are comments

# comments are not read by the computer, they are meant for programmers
# to explain what each part of the code does

# identify_pizza() is a python function
# its role is to identify the type of pizza that is eaten
# and to estimate the time in seconds to eat that pizza
# based on the number of cheese strips, pepperoni slices 
# and pineapple chunks 

# this function takes 3 integers as inputs
# this outputs a python dictionary with the type of pizza 
# and the time it took to eat the pizza

# note that the block inside the function is indented

def identify_pizza(cheese=0, pepperoni=0, pineapple=0):

	# these are two local variables 
	type_of_pizza = ""	# type of pizza (string)
	eating_time = 60.0	# eating time in seconds (float)

	# the following are decision statements (if/elif/else)
	# the "and" operator means that a statement is true
	# only if all of the conditions are true
	# note that there is a colon ':' at the end of each statement
	# and each executable block of code is indented
	
	if cheese == 0 and pepperoni == 0 and pineapple == 0:
		type_of_pizza = "tomato pizza"

	# elif is short for else-if
	elif cheese > 1 and pepperoni == 0 and pineapple == 0:
		type_of_pizza = "cheese pizza"

	elif cheese > 1 and pepperoni > 1 and pineapple == 0:
		type_of_pizza = "pepperoni pizza"

	elif cheese > 1 and pepperoni > 1 and pineapple > 1:
		type_of_pizza = "hawaiian pizza"

	# else is only used if all the "if and elif statements" are false
	else:
		type_of_pizza = "inventive pizza"

	# eating time is calculated by adding values together
	eating_time = eating_time + 0.1*cheese + 1.0*pepperoni + 2.0*pineapple

	# the function identify_pizza() returns a dictionary
	return {"type of pizza": type_of_pizza, "eating time (seconds)": eating_time}

# we call identify_pizza() with 100 cheese slices, 10 pepperoni slices, 
# and 0 pineapple chunks
# the returned dictionary is assigned to the variable result
result = identify_pizza(100,10,0)

print(result)
