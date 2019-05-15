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

print """
SD3:  We've used the label "commands", but these are usually called 
      "functions" and "methods".  Search online to see what other people
      do to define these.  Do not fret if it is confusing -- it is normal
      for programmers to confuse you with vast extensive knowledge.

Per w3schools.com, https://www.w3schools.com/python/python_functions.asp
A function is a block of code which runs only whnen it is called.  You 
can pass data (parameters, arguments) into a function.  A function can
return data as a result.  In Python, a function is defined using the  def
keyword.
"""

# "Function" example from w3schools
def my_fxn():
    print "Foo Bar Baz Quux"

my_fxn()
my_fxn()

print """
GeeksForGeeks
https://www.geeksforgeeks.org/difference-method-function-python/
talks about Difference between Method and Function in Python.  Sorry for
any mangling  do here.

Python Method:
 - Called by name, but associated to an object (dependent).
 - A method implicitly is passed the object upon which it was invoked [so,
argv() passes the scriptname].
 - Method may, or may not, return data.
 - A method can operate on the data (instance variables) that is contained
by the corresponding *class*.

Python Function:
 - Called by its name, but independent -- not asssociated to an object.
 - Functions may have different parameters, or none at all.  If any data
   (parameters) are passed, it has to be explicit (not implicit).
 - Function may, or many not, return data.
 - Function does not deal with Class and its "instance concept".
"""
