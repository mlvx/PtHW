print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# Study Drills
# SD4:  Related to escape sequences, find out why the last line
# of output has  '6\'2"'  with that \' sequence.  See how the 
# single-quote needs to be escaped, because otherwise it would
# terminate the string?

print
print "Testing escape:  height = %r (raw/rep) height = %s (str)" % (
    height, height)

# It's actually interesting.
# height = 6' 1"  -->  '6\' 1"'
# height = 73"    -->  '73"'
# height = 6'     -->  "6'"
# Formatted with %r, it prefers to surround with  ''  but will adapt
# and surround with  ""  if the input includes a '.  If the input
# includes both kinds of quotation marks, it will surround with  ''
# and escape the interior  '  mark.
