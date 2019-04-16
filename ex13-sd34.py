# from sys import argv
# 
# script, first, second, third = argv
# 
# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second 
# print "Your third variable is:", third 

# Study Drills
# SD3:  Combine  raw_input  with  argv  to make a script that
#       gets more input from a user.

from sys import argv

filename, argvar1, argvar2 = argv
print "So:", filename + ", " + argvar1 + ", and" , argvar2 + ".  Interesting."
pie_flavor = raw_input("What flavor of pie do you prefer? ")
icecream_flavor = raw_input("And, what kind of ice cream do you like? ")
print "I bet you'd like some", pie_flavor, "pie topped with some" , \
    icecream_flavor, "ice cream, wouldn't you?"
print "Sorry.  Fresh out."

# SD4:  
