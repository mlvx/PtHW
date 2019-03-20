# Here's some new strange stuff, remember type it exactly.

# Sets text string var "days" with abbrev. days of the week,
# in one long string; spaces separating different days.  This
# outputs all on one line.
days = "Mon Tue Wed Thu Fri Sat Sun"
# Sets text string var "months" with abbrev. months, Jan.-Aug.
# Months are separated by newlines,  \n  and each one prints 
# on a differnet line.
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Prints a text string, followed by a text string stored in 
# var "days".  Surprisingly, it works even when a  +  replaces
the comma.
print "Here are the days: " , days
# Prints a text string, followed by a text string stored in 
# var "months".
print "Here are the months: ", months

# Text string surrounded by triple-quotemarks -- i.e., the 
same single-quote or double-quote typed three times makes
eveything inside the triple-quote a text string; linebreaks 
are preserved.
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

# Study Drills
# SD1: Do checks of your work, write down your mistakes, do better on the next exercise.
# No output errors on this one.  I will add comments to each line and call it "good".
