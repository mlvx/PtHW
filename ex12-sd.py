import os
import sys

# age = raw_input("How old are you? ")
# height = raw_input("How tall are you? ")
# weight = raw_input("How much do you weight? ")

# print "So, you're %r old, %r tall and %r heavy." % (
    # age, height, weight)

# Study Drills
# These four study drills are about learning to use PyDoc.
# No need for four separate files, it turns out.
# Thank you, StackOverflow, for the suggestion of using
# raw_input()  to pause pages of output.
# https://stackoverflow.com/questions/577467/pause-in-python

print """ - - - - - - - - - - - - - - -
# SD1:  In your Terminal, type  pydoc raw_input  and read what it says.

Ok, I read it.  Looks like it's a built-in function that waits for the 
user to type some input, then press [Enter]; at which point it strips 
off the trailing newline, and -- It doesn't really say what happens 
next, but we (royally) infer that it uses the typed input in later 
instructions.
    There is an option to include a prompt, like "Name? " etc.  And,
if somehow the user causes an End-Of-File (like ctrl-D), then Python
raises an EOFError. """


raw_input("Press 'Enter' to continue.")
print """ - - - - - - - - - - - - - - -
# SD2:  Quit from PyDoc by typing 'q'.

Sometimes I forget what the target readership is of this book.  And
then I feel a bit ashamed that I didn't pursue this 20 years ago. """


raw_input("Press 'Enter' to continue.")
print """ - - - - - - - - - - - - - - -
# SD3:  Look online for what the  pydoc  command does.

The Socratica YouTube video on PyDoc is fun and informative:
    https://www.youtube.com/watch?v=URBSvqib0xw
So, PyDoc is Python's documentation generator and online help system.
    https://docs.python.org/2/library/pydoc.html
"The pydoc module automatically generates documentation from Python
modules.  The documentation can be presented as pages of text on the
console, served to a Web browser, or saved to HTML files."

That's actually kinda cool.

Okay, it's got its own pagination system and pager.
Use the  -w  flag to write the documentation to an HTML file in the
current directory (instead of showing text on the terminal).
Use the  -k  "keyword" flag to search the synopsis lines of available
modules.  (Synopsis line is the first line of its documentation string.) """


raw_input("Press 'Enter' to continue.")
print """ - - - - - - - - - - - - - - -
# SD4:  Use pydoc to also read about  open, file, os,  and  sys.  Even
though I won't understand most of it, I should read it and take notes
on interesting things.

Ok; here goes. 
:::::::::: ::::::::::"""


raw_input("Press 'Enter' to continue.") # pydoc open
print """
pydoc open   - A built-in function in the module __builtin__.
Use like    open(...)
            open(name[, mode[, buffering]]) -> file object
(The stuff in [square brackets] is optional.)
Opens a file by using the  file()  type, and returns a "file object"
(whatever that is).  This is the preferred way to open a file.  See
file.__doc__  for more info. """

raw_input("Press 'Enter' to continue.")
print """
pydoc file.__doc__ = class str(basestring)
"Return a nice string representation of the object.  If the argument
 is a string, the return value is the same object."

Looks like a lot to learn; but I gotta try the "capitalize" ..., uh, 
what are these -- "methods"?  "functions"?  Learn that later.
"""

foo="this string var has only lowercase letters"
print foo
print foo.capitalize()
print foo.center(80)
raw_input("Press 'Enter' to continue.")

print """
Holy guacamole.  The 'capitalize() thing worked worked!  Joyfeel.
My first attempt at combining 'center' with 'capitalize' didn't 
work.  Something to learn soon.

These look powerful.  I see math ones, comparison ones, "GetNewArgs",
formatting ones, size evaluators...  Not clear how the "file" part 
fits in, yet.  This is gonna be fun.
:::::::::: ::::::::::"""

raw_input("Press 'Enter' to continue.") # pydoc file
print """
pydoc file   - A built-in function in the module __builtin__.
class file(object)

Use like    file(name[, mode[, buffering]) -> file object
Open a file.  Possible modes: 'r' (read-only, default), 'w' (write),
or 'a' (append).  File is created (if it doesn't already exist) when
opened for writing or appending.  If it exists, it will be truncated
when opened for writing.
   Add 'b' to the mode for binary files.  (Egad!)  Add '+' to the
mode for simultaneous reading and writing.  (Egad!)
   Some stuff about buffering...
   Add 'U' to the mode for universal newline support.  But, 'U' 
cannot be combined with 'w' or '+'.
   The preferred way to open a file is with the  open() function
[which we talked about above].

Some methods:  __delattr__  (deletes an attribute?)
__enter__   __exit__   __getattribute__
__close__   __fileno__   __flush__   __next__

I gotta try the "__readline__" one.  I'll use  ex1.py  which was 
the "Hello World" one.  
Okay, that didn't work.  I ended up creating a new file to use for
this, called 'testingfile'.  I think I'm learning it, thanks to more
documentation:  https://docs.python.org/2/tutorial/inputoutput.html

I needed to use quotation marks, and maybe whitespace around the 
'=' definition operator.  Trying again.
"""

bar = file('testingfile')
print bar.readline()

print"""
Ok!  That's working.  Ish.  Moving forward.
:::::::::: ::::::::::"""

raw_input("Press 'Enter' to continue.") # pydoc os
print """
pydoc os     - Operating System routines
Lives at     /usr/lib/python2.7/os.py
Module docs at    http://docs.python.org/library/os

Looks like this gives tools for dealing with the host OS:  path,
current directory, pathname separator, devnull, etc.

"Programs that import and use 'os' stand a better chance of being
portable between different platforms.  Of course, they must then
only use functions that are defined by all platforms (e.g., unlink
and opendir), and leave all pathname manipulation to os.path
(e.g., split and join).

So,  os  is a module; and it has several classes and methods,
it looks like.  Some of them are inherited from others.  Like,
__delattr__ is inherited from  BaseException.

Data descriptors, like  st_ctime  is a string with time of last
change.  Not sure how it's different from  st_mtime  which is 
time of last modification.

Some of the familiar math stuff, like __add__(...)  etc.
Hm.  There's builtin "create a pipe" functionality.
Looks like you have your basic shell commands here -- rmdir, etc.

I've got to try  urandom(n)  "Returns n random bytes suitable for
cryptographic use" (returned as a string object).
"""
baz = os.urandom(64)
print baz

print """
Well, that worked (once I put "os." in front of "urandom(64)".
Thank you, https://docs.python.org/2/  !!!
:::::::::: :::::::::: """

raw_input("Press 'Enter' to continue.") # pydoc sys
print """
pydoc sys    - Another builtin module.

"This module provides access to some objects used or maintained
by the interpreter, and provides access to functions that 
strongly interact with the interpreter."  (Not an exact quote,
but close.)

There are "dynamic objects".  "argv[]"  I've seen before.
"path[]"  I might have seen before.  "displayhook" sounds 
interesting.    stdin  -- standard input file object; used by
raw_input() and input().  (Weird, I thought raw_input was getting
string objects, not file objects?)

stdin, stdout, stderr:  "By assigning other file objects (or
objects that behave like files) to these, it is possible to
redirect all of the interpreter's I/O."  Egad.

And there are "static objects" like "getrecursionlimit()".  Ok,
I gotta try that.  (Helps if I remember to put "import sys" at
the beginning of the file.)
"""
quux = sys.getrecursionlimit()
print "sys.getrecursionlimit() reports: " , quux

raw_input()
print """
Holy smackerel -- 1000 recursions?  I'm surprised it's not some
kind of power of two, or power of two minus one.  Maybe it's 
really 1023 but they limit it to 1000 for safety.

Ok, I feel like I've done enough with Study Drill 4.  I'm sure 
that I'll end up reading more of this stuff, in more depth, 
later."""
