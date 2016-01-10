#!/usr/bin/python
# Variables and Names

# Sets variable to 100
cars = 100
# Sets variable to 4
space_in_a_car = 4
# Sets variable to 30
drivers = 30
# Sets variable to 90
passengers = 90
# Sets new vaiable to integer using previously set variables
cars_not_driven = cars - drivers
# Sets variable to integer using previously set variables
cars_driven = drivers
# Sets variable to integer using preciously set variables
carpool_capacity = cars_driven * space_in_a_car
# Set variable to integer using previously set variables
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", divers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Study drill
#
# I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
# Remember that 4.0 is a floating point number. It's just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point.
# Write comments above each of the variable assignments.
# Make sure you know what = is called (equals) and that it's making names for things.
# Remember that _ is an underscore character.
# Try running python from the Terminal as a calculator like you did before and use variable names to do your calculations. Popular variable names are also i, x, and j.
