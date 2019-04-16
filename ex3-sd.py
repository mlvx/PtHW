print "I will now count my chickens:"

# Line 4 follows Order of Operations, to my surprise.  30/6=5.  25+5=30.
print "Hens", 25 + 30 / 6
# Line 6.  25*3=75.  75 mod 4 = 3.  100-3=97.
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

# Study Drills

# SD1.  Above each line, write a comment explaining what the line does.
# No, I'm not doing that; useless comments.  I'll do two of them, and trace 
# the orders of operaitons.

# SD2.  Use Python as an interactive calcluator.
# Done.  Fun.

# SD3.  Find something you need to calculate.  Write a new .py file to do it.
# See ex3-sd3-weight.py.

# SD4.  Notice the math seems "wrong" -- no fractions, only whole numbers.  
#	Research "floating point" numbers.
# This ended up being more interesting than I'd expected.  It's an issue with
# binary arithmetic.  Just as in decimal, you can't really represent 1/3
# accurately (0.3 repeating), in binary you can't rep decimal 1/10 accurately.
# You can only do an approximation.  You get 53 bits of approximation -- good
# enough for most things but can have unexpected results (rounding etc.).
# https://docs.python.org/2/tutorial/floatingpoint.html

# SD5.  Rewrite ex3.py to use floating point numbesr so it's more accurate 
#	(hint: 20.0 is floating point).
# See ex3-sd5-floating.py.

# 2019-04-16	Edited to reflect conventionally preferred style, as at:
# https://www.python.org/dev/peps/pep-0008/
