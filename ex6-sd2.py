x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e 

# Exercise 6 Study Drills

# SD1: Write an explanatory comment above each line.
# SD2: Find all four places where a string is put inside a(nother) string.
# Lines 4 (two instances), 9, and 10.  Lines 13 and 15 don't count -- 
# "hilarious" is a Boolean, not a string.  Line 20 doesn't count -- it's
# a concatenation of two strings, not putting one string inside another.
