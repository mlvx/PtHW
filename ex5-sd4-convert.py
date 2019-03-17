name = "Zed A. Shaw'tee"
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Metric conversions
height_metric = height * 2.54
weight_metric = weight / 2.2

print "Let's talk about %r." % name
print "He's %s inches tall.  That's about %i centimeters." % (height, round( height * 2.54) )
print "He's %r pounds heavy, which is about %i kilograms." % (weight, round(weight / 2.2) )
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

# Study Drills

# SD1:  Change all the variables so there isn't the    in front.
# SD2:  Try more format characters, like %r -- a very useful one.  It's like
#       saying "print this no matter what".
# SD3:  Search online for all the Python format characters.
# SD4:  Write some variables that convert the inches and pounds to cm and kg.
#       Don't just type in the measurements; work out the math in Python.
# First, I created new variables to hold the metric values; then I realized
# I could perform the calculation in the print statement -- no need to make
# new vars.  I didn't like the inches-to-cm result because if Shaw's height
# is 187.96 cm, you might as well call it 188 cm.  So I ended up looking up
# the  round()  function.  Which, actually, Shaw mentions in the "Common 
# Student Questions" section.  
