from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second 
print "Your third variable is:", third 

# Study Drills
# SD1:	Try giving fewer than three arguments when running, and explain the 
# resulting error.

print """
This script expects the scriptname and three additional arguments (if we
consider the scriptname to be an argument).  When I run the script with
only two args, the errmsg is "ValueError: need more than 3 values to unpack".

When I run it with only one arg, the errmsg is "ValueError: need more than
2 values to unpack".

When I run it with no arguments (as I did several times before reading 
further in the book, d'oh!), the errmsg is "ValueError: need more than 1
value to unpack".  (I admit I'm a little impressed they took the time to get
the pluralization right.)

When I run it with five arguments, the errmsg is "ValueError: too many 
values to unpack".

From this, we conclude that the "argv" function in the "sys" module counts
the arguments on the command line, and throws a flag if the quantity of args
does not match the quantity in the argv statement.
"""
