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
# SD6:  Run  pydoc file  and scroll down until you see the  read()  command
#       (method / function).  See all the other ones you can use?  Skip the
#       ones that have  __  (two underscores) in front because those are
#       junk.  [?]  Try some of the other commands (methods / functions).
# SD7:  Start python again and use  open  from the prompt.  Notice how you
#       can open files and run  read  on them right there?
