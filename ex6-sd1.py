# Defines var 'x' as text string, with embedded "decimal" format for external number.
x = "There are %d types of people." % 10
# Defines var 'binary' as text string.
binary = "binary"
# Defines var 'do_not' as text string.
do_not = "don't"
# Defines var 'y' as text string, with embedded "string" format for 2 external numbers.
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints the "There are 10 types of people" variable.
print x
# Prints the "Those who know binary..." variable.
print y

# Prints a text string, with the "There are 10 types..." string var, formatted
#    with "raw/rep" converter (surrounds with single quotation marks).
print "I said: %r." % x
# Prints a text string, with the "Those who know binary..." string var, formatted
#    with "string" converter.  This doesn't surround with quotation marks, which
#    in this case are included in the text string of the print statement ('%s').
print "I also said: '%s'." % y

# Defines 'hilarious' as a Boolean var with a value of "False".
hilarious = False
# Defines 'joke_evaluation' as a text string, that formats an arbitrary var with 
#    the "raw/rep" converter.
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints "Isn't that joke..." string var, calling the Boolean "False" var formatted
#    with "raw/rep" converter.
print joke_evaluation % hilarious

# Defines var 'w' as text string.  (W is short for "west", obvsly.)
w = "This is the left side of..."
# Defines var 'e' as text string.  (E is short for "east", obvsly.)
e = "a string with a right side."

# Prints a concatenation of the two text string vars defined just above here.
#    Note that the output does not have a space between the two vars.
print w + e 

# Exercise 6 Study Drills

# SD1: Write an explanatory comment above each line.
# Ugh.  Really?  Ok.
