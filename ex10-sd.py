tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Ex. 10 - Study Drills
# SD1: Memorize the escape sequences, with flash cards.
# In progress.

# SD2: Use ''' instead of """ on lines 5 and 10.  Can you see why
#      that might be better?
# There's no difference in the output.  Maybe  '''  is easier to 
# spot than  """  when you're reading code?  I'll have to try both
# for a while, and see if I have a preference.

# SD3: Combine escape sequences and format strings to create a
# more complex format.
# SD4: Combine  %r  with double-quote and single-quote escapes, 
# and print them.  Compare  %r  with  %s.  Notice how  %r  prints
# it the way you'd write in a your file, and  %s  displays it in
# more conventionally.

# Variables to print
x = "\n"	# These vars must precede lines that call it.
s1 = "There\'s a difference between a" + x + "%s" + x + "%r"
s2 = "\"slash\" character (/) and a"
s3 = "\'backslash\' character (\\)."
s4 = 'The  \'/\'  is the root in a *nix system,' + x + "%s"
s5 = 'and the  \"\\\"  is the escapce leader character.'

print
print s1 % (s2, s3)
print s4 % s5

# It's interesting how the escaped backslashes get displayed
# when formatted with %r.
