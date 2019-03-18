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
print w , e # Testing diff '+' vs ','

# Exercise 6 Study Drills

# SD1: Write an explanatory comment above each line.

print """
SD2: Find all four places where a string is put inside a[nother] string.
Line 4 (two instances): y = "Those who know %s and those who %s." % (binary, do_not)
Line 9: print "I said: %r." % x
Line 10: print "I also said: '%s'." % y
"""

print """
SD3: Are you sure there are only four places?
Lines 13 and 15 don't count --  "hilarious" is a Boolean, not a string.
Line 20 doesn't count -- it's a concatenation of two strings, not
putting one string inside another.
"""

print """
SD4: Explain why adding the two strings /w/ and /e/ with /+/ makes a longer string.
"""
