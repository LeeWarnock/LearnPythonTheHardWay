#!/usr/bin/python
#: Author               Curtis Mckee
#: Description          Learn Python the Hard Way - Exercise 11: Asking Questions
#: Email                cmckee.dev@gmail.com

print "How old are you?"
age = raw_input()
print "How tall are you?"
height = raw_input()
print "How much do you weigh?"
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# Study drills
# 
# Go online and find out what Python's raw_input does.
# Can you find other ways to use it? Try some of the samples you find.
# Write another "form" like this to ask some other questions.
# Related to escape sequences, try to find out why the last line has '6\'2"' with that \' sequence. See how the single-quote needs to be escaped because otherwise it would end the string?

print "How many exercises have you done so far?"
exer = raw_input()

print "Great!", 52 - int(exer), "exercises left!"
