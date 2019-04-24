from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# Study Drills
# SD1 (comment each line), SD2 (research online documentation):
# See file ex15-sd12.py.
#
# SD3:  We've used the label "commands", but these are usually called 
#       "functions" and "methods".  Search online to see what other people
#       do to define these.  Do not fret if it is confusing -- it is normal
#       for programmers to confuse you with vast extensive knowledge.
# SD4:  Get rid of the part from lines 10-15 where you use  raw_input  and
#       try the script without them.
# SD5:  Use only  raw_input  and try the script that way.  Think of why one
#       way of getting the filename would be better than another.
# SD6:  Run  pydoc file  and scroll down until you see the  read()  command
#       (method / function).  See all the other ones you can use?  Skip the
#       ones that have  __  (two underscores) in front because those are
#       junk.  [?]  Try some of the other commands (methods / functions).
# SD7:  Start python again and use  open  from the prompt.  Notice how you
#       can open files and run  read  on them right there?
# SD8:  Have your script also do a  close()  on the  txt  and  txt_again
#       variables.  It's important to close files when done with them.
