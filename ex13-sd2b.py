# from sys import argv

# script, first, second, third = argv

# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second 
# print "Your third variable is:", third 

# Study Drills
# SD2, part B:	Write a script that has more arguments (than the orginal script).

from sys import argv

scriptname, arg1, arg2, arg3, arg4, arg5 = argv
c = ","  # Quick-n-dirty way to put [c]ommas in the output, I hope.

print "You ran", scriptname + ", the 'zeroth' argument, with '%s' as \
the 'first' argument." % arg1
print "Your last argument was " + arg5 + "."
print "In between", arg1, "and", arg5 + ", you had", arg2 + c, arg3 + c, "and", \
    arg4 + ", in that order."

# Thanks, developer.rhino3d.com, for the tip about using a backslasp to break
# up long lines!  Hmm... I wonder if that works for comments, too?  Gotta \ 
# test it.
# Answer:  No, it does not work.  I guess it cannot work, since Python ignores
# everything after the hashsign.
# whitespace after the backslash is included in the output.  I shouldn't be
# surprised, since it's inside the quotation marks.
