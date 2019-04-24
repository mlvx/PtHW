from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

# print "Type the filename again:"
# file_again = raw_input("> ")
# 
# txt_again = open(file_again)
# 
# print txt_again.read()

# Study Drills
# SD1 (comment each line), SD2 (research online documentation):
# See file ex15-sd12.py.
# SD3:  We've used the label "commands", but these are usually called 
#       "functions" and "methods".  Search online to see what other people
#       do to define these.  Do not fret if it is confusing -- it is normal
#       for programmers to confuse you with vast extensive knowledge.
# SD4:  Get rid of the part from lines 10-15 where you use  raw_input  and
#       try the script without them.
# Done.  It runs fine, but uses only the variables populated with argv when
# first running the script.
