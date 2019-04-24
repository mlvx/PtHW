# from sys import argv
# 
# script, filename = argv
# 
# txt = open(filename)
# 
# print "Here's your file %r:" % filename
# print txt.read()

print "Type the filename:"   # Don't need 'again' in this context.
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# Study Drills
# SD1 (comment each line), SD2 (research online documentation):
# See file ex15-sd12.py.
# SD3:  "Commands", "functions", "methods":  Do some research.
# Done; work in progress.  See file ex15-sd3.py.
# SD4:  Get rid of the part from lines 10-15 where you use  raw_input  ...
# Done (commented out).  The script runs fine, but uses only the variables
# populated with argv when first running the script.
#
print """
SD5:  Use only  raw_input  and try the script that way.  Think of why one
      way of getting the filename would be better than another.

The script runs fine using only  raw_input  and not  argv.
Two ways of getting the filename:  argv and raw_input.

argv may be less prone to user error (depending on how the script is
launched).  argv also has less flexibility than raw_input.  On the other
hand,  raw_input  has flexibility for handling unexpected complications.
