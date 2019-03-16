name = "Zed A. Shaw'tee"
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %s inches tall." % height
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

# Study Drills

# SD1:  Change all the variables so there isn't the my_ in front.
# SD2:  Try more format characters, like %r -- a very useful one.  It's
#       like saying "print this no matter what".

# SD3:  Search online for all the Python format characters.

print '''
Exercise 5, Study Drill 3:  Search online for all the python format characters.

Ok, ignoring the "Format Specification Mini-Language" for now --
https://docs.python.org/2.7/library/string.html#formatspec 
That's beyond the scope of the question.  (Pretty nifty though.)

Likewise, we'll skip for now the HTML Formatter functionality --
https://docs.python.org/2.7/library/formatter.html
Awesome, but let's save it for when we actually have a clue.

Wow.  The Python 2.7 Docs index has about 42-odd entries beginning with 
"format".

Here we go:
https://docs.python.org/2.7/library/stdtypes.html#index-25

Paraphrasing/Quoting:
    String and Unicode objects have one unique built-in operation:
the  %  operator (modulo).  This is a.k.a. the string /formatting/
or /interpolation/ operator.
   Given  format % values  (where  /format/  is a string or Unicode
object),  %  conversion specs in  /format/  are replaced with zero 
or more elements of  /values/.  [Similar to  sprintf()  in C.]
    If  /format/  is a Unicode object, or if any of the objects being
converted vis  %s  are Unicode objects, then the result will also be
a Unicode object.

    If  /format/  requires a single argument,  /values/  may be a 
single non-tuple object.  [Learn 'tuple' later.]  Otherwise,  /vaules/
must be a tuple with exactly the number of items spec'd by the format
string, or a single mapping object (like a dictionary).

    A [format] conversion specifier has two or more characters, and 
the following components, which must occur in this order:
    (1) %
    (2) Optional mapping key, consisting of a parenthesised seq. of
        characters -- like,  (somename)
    (3) Optional conversion flags, which can mod some conversion types.
    (4) Optional minimum field width; if spec'd as  *  (splat), then
        the actual width is read from the next element of the tuple in
        /values/  and the object to convert comes *after* the minimum 
        field with and (optional) precision.
    (5) Optional precision, spec'd as a  .  (dot) followed by the 
        precision.  If spec'd as  *  (splat), then the actual width 
        [wait, width?? I thought we were on "precision" now??] is read
        from the next element of the tuple in  /values/  and the value
        to convert comes *after* the precision.
    (6) Optional (and apparently ignored) length modifier.
    (7) Conversion type (not marked optional, so I guess it's mandatory).

I'm going to have to play with these options to really grasp them --
for now, here's the list of possible format characters.

%d  Signed integer decimal.             %i  Signed integer decimal.
%o  Signed octal value.                 %u  Obsolete -- same as %d.
%x  Signed hexadecimal (lowercase).     %X  Signed hexadecimal (uppercase).
%e  Floating-point exponential (lc).    %E  Floating-point exponential (uc).
%f  Floating-point decimal format.      %F  Floating-point decimal format.
    Note:  If var. is assigned as  int, formatting as F-P will not make it
    behave like F-P in a calculation.  42/9 = 4.000000, but 42.0/9 = 4.666667
%g  F-P format:  lc exponential, if exp. is less than -4 or not less than
    [its?] precision; decimal format otherwise.
%G  Like %g, but with uppercase exponential format instead of lowercase.
%c  Single character (accepts integer or single character string).
%r  'Raw' or 'Representation' -- Converts any Python object via repr().
%s  String -- Converts any Python object via str().
%%  No argument is converted; places a  %  char. in the output.

There also are conversion flag characters:
'#' Uses "alternate form" -- leading zeroes, forced decimal points, etc.
'0' Adds padding with zeroes for numeric values.
'-' Left-adjustment; overrides the  0  flag, if both are present.
' ' (A "space" character)  Puts a blank before a positive number
    (or empty string) produced by a signed format conversion.
'+' Puts a sign char. (+/-) before the conversion (overrides ' ' flag).

'''

# SD4:  Write some variables that convert the inches and pounds to cm and kg.
#       Don't just type in the measurements; work out the math in Python.
