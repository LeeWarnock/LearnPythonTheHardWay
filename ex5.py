#!/usr/bin/python
#: Author                   Curtis Mckee
#: Description              Learn Python the Hard Way - Exercise 5: More Vaiables and Printing
#: Email                    cmckee.dev@gmail.com

name = "Curtis Mckee"
age = 27
height = 70 * 2.54 #inches converted to Centemeters
weight = 125 * 0.453592 #lbs converted to kiliograms
eyes = "Blue"
teeth = "White"
hair = "Light Brown"

print "Let's talk about %s." % name
print "He's %d centemeters tall." % height
print "He's %d pounds." % weight
print "That's not heavy at all."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d and %d I get %d." % (age, height, weight, age + height + weight)

# Study drills
#
# Change all the variables so there is no my_ in front of each one. Make sure you change the name everywhere, not just where you used = to set them.
# Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do not just type in the measurements. Work out the math in Python.
# Search online for all of the Python format characters.
# Try more format characters. %r is a very useful one. It's like saying "print this no matter what."
