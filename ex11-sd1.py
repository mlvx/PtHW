# print "How old are you?",
age = raw_input("How old are you in years? ")
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# Study Drills
print """
SD1: Go online and find out what Python's  raw_input()  does.

Summary:  "raw_input()" is a Built-in Function that gets a string
from standard input (typed in the terminal), strips the trailing
newline, and passes it to the interpreter without interpretation.
(I expect that sentence to make sense to me in the near future.)
Optionally, one can put a prompt string inside the parens, thus:
raw_input("This will show up as a prompt ")
"""

# PyDoc finds nothing for  raw_input  and  raw_input()  causes problems
# because of the parens, and requiring them to be escaped would be 
# psychotic, so I think PyDoc has nothing on raw_input.  PyDoc has a 
# bit on  input()  so that's a start:
#    Read a string from standard input, stripping the trailing newline.
#    If user hits EOF, raise EOF error.  Uses GNU readline, if enabled.
#    Prompt string is printed sans trailing newline before reading.
# 
# Interestingly, using PyDoc -k to search for keyword "input", I see
# that "raw_input" is dropped in Python3:
#    lib2to3.fixes.fix_raw_input - Fixer that changes raw_input(...) 
#    into input(...).
# 
# https://docs.python.org/2/library/functions.html?highlight=raw_input#raw_input
# raw_input([prompt])  is a Built-in Function.
#    If the "prompt" arg is present, it is written to sdout sans 
#    trailing NL.  The function then reads a line from input, converts
#    it to a string (stripping a trailing newline), and returns that
#    string.  Ok, this is assuming interactive mode.  Ah, but I see 
#    that the interpreter more or less enters interactive mode to 
#    parse a script.
# Note: to read ‘raw’ input line without interpretation, you can use
# the built-in function raw_input() 
