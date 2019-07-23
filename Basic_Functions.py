
###############################################################################
# 1 Demo: Writing a Basic Function

# This is a function that takes a name as an argument(input) and returns(output) "Hello [name]!"

# Defining the function
def greet(name):
  return "Hello " + name + "!"

# Calling the function
# greet("Jessica")

# Call the function and print it to the console
#print(greet("Jessica"))

###############################################################################
# 2 Buddy Program: Basic Function

# Define a function that takes an name as an argument(input) and returns(output) the compliment, "[name] is an awesome human being!"


# Call the function and print it to the console


##############################################################################
# 3 Demo: Functions with Multiple Arguments

# Define the function!
def personalized_age_check(name, age):
  if age >= 18:
    return "Congratulations " + name + "! You're old enough to vote."
  else:
    time_left = 18 - age
    return "Sorry, " + name + ". You can't vote for another " + str(time_left) + " years."

# Call the function and print tthe result to the console
# print(personalized_age_check("Inari", 28))
# print(personalized_age_check("Max", 14))
# print(personalized_age_check("Aaron", 444))

##############################################################################
# 4 Buddy Program: Function with Multiple Arguments

# Mini Mad-Libs

# Define a function that has the parameters celebrity_name and an adjective
# It should return "[celebrity_name], once that [adjective] music comes on, it's time to shut down your acceptance speech!"



# Call the function and print the result to the console with 3 different sets of arguments

