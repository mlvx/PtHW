# from sys import argv
# 
# script, first, second, third = argv
# 
# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second 
# print "Your third variable is:", third 

# Study Drills
# SD2, part A:	Write a script that has fewer arguments (than the orginal script).

from sys import argv

scriptname, var_one, var_two = argv

print "Your script is named %s." % scriptname
print "The first argument was", var_one + "."
print "The last argument was %r." % var_two
