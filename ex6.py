#!/usr/bin/python
#: Author               Curtis Mckee
#: Description          Learn Python the Hard Way - Exercise 6: What was that?
#: Email                cmckee.dev@gmail.com

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Study drills
#
# Memorize all the escape sequences by putting them on flash cards.
# Use ''' (triple-single-quote) instead. Can you see why you might use that instead of """?
# Combine escape sequences and format strings to create a more complex format.
# Remember the %r format? Combine %r with double-quote and single-quote escapes and print them out. Compare %r with %s. Notice how %r prints it the way you'd write it in your file, but %s prints it the way you'd like to see it?
