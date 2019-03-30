print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# Study Drills
print """
SD1: Go online and find out what Python's  raw_input()  does.

PyDoc finds nothing for  raw_input  and  raw_input()  causes problems
because of the parens, and requiring them to be escaped would be 
psychotic, so I think PyDoc has nothing on raw_input.  PyDoc has a 
bit on  input()  so that's a start:
   Read a string from standard input, stripping the trailing newline.
   If user hits EOF, raise EOF error.  Uses GNU readline, if enabled.
   Prompt string is printed sans trailing newline before reading.

Interestingly, using PyDoc -k to search for keyword "input", I see
that "raw_input" is dropped in Python3:
   lib2to3.fixes.fix_raw_input - Fixer that changes raw_input(...) 
   into input(...).


"""
