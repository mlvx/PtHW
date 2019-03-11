name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

# Study Drills

# SD1:  Change all the variables so there isn't the    in front.
# Done.  Too easy, in Vim.

# SD2:  Try more format characters, like %r.
# SD3:  Search online for all the Python format characters.
# SD4:  Write some variables that convert the inches and pounds to cm and kg.
#       Don't just type in the measurements; work out the math in Python.
