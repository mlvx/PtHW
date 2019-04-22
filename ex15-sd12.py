# Module 'sys' has file utilities etc.  Load the 'argv' function
# that's part of 'sys'.
from sys import argv

# Initializes two variables -- 'script' and another named 'filename' -- and
# uses 'argv' to set their value, based one what the user typed to run the
# script (in this case, should be 'ex15.py' and 'ex15_sample.txt'.
script, filename = argv

# Initializes a var., 'txt', and sets its value to be the "file object" that
# results when 'ex15_sample.txt' (because that's what should be in the
# 'filename' var., as set by argv when script launched) is opened.
txt = open(filename, rt)

# Pretty self-explanatory.  Prints a message and formats the contents of the
# 'filename' var with quotation marks, in raw/rep format style.
print "Here's your file %r:" % filename
# Reads the contents of the "file object" stored in the var. named "txt",
# and prints those contents to the screen.
print txt.read()

# Message instructing user about what to type.
print "Type the filename again:"
# Creates a variable named 'file_again', and sets its value to be typed in by
# the user; and puts a helfp prompt that looks like an arrow showing where to
# begin typing..
file_again = raw_input("> ")

# Creates a var. named 'txt_again', and sets its value to be the file object
# that gets opened by open() based on what input the user put in) (should be
# ex15_sample.txt).
txt_again = open(file_again)

# The var. 'txt_again' contains the file object 'file_again' (obtained via
#  open(var-assigned-via-raw_input) ), and this line calls  read()  on that
# file object; and prints out the results of the  read()  operation.
print txt_again.read()

# Study Drills
# SD1:  Above each line, write out in English what it does.
# Done; see above.
#
# SD2:  If you are not sure, ask someone for help or search online.  Often,
#       searching for "python FOO" will find answer for what that FOO does
#       in Python.  Try searching for "python open".
# There are multiple decent explanations of "python open".  I like this one:
# https://www.w3schools.com/python/python_file_handling.asp
#
# The key function for working with file in Python is the  open()  function.
# The  open()  function takes two parameters --  filename  and  mode .
# Four possible modes:  "r" is Read (default).  Opens the file for reading,
# and errors if the file does not exist.  "a" is Append.  Creates file if it
# is not found.  "w" is Write; creates if not found.  "x" simply creates the
# spec'd file, and errors if the file exists already.
#
# You also can spec text mode "t" or binary mode "b".
#
# "r" mode is default.  These two lines behave equivalently:
#      f = open("foo.txt")
#      f = open("foo.txt", "rt")
# I'm not clear whether the quotation marks are necessary.  They show up in
# the online explanations I'm looking at, but they were omitted in the 
# exercise.  Will test.
# Actually, calling open() on a variable, you can't use quotation marks
# around the filename part; and if you're specifying a mode, you do need to
# use quotemarks around the mode argument.
