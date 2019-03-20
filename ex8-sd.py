# Defines a string var called "formatter", and assigns four
# instances of the %r "raw/rep" format converter characters.
formatter = "%r %r %r %r"


# Prints the "formatter" string, subbing in the numerical
# values in parentheses.  Since they're numbers, there are no
# quotation marks in the output.
print formatter % (1, 2, 3, 4)

# Prints the "formatter" string, subbing in the text strings
# in parentheses.  Since they're text, there are single
# quotation marks around each element (tuple?) of the output.
print formatter % ("one", "two", "three", "four")

# Prints the "formatter" string, subbing in the Boolean values
# in parentheses.  Since they're booleans, there are no 
# quotation marks in the output.
print formatter % (True, False, False, True)

# Prints the raw representation of the "formatter" variable;
# prints it four times.  That ends up being '%r %r %r %r' * 4
# including the single quotation marks.  I guess the raw 
# representation of a format converter character sequence is
# the literal sequence, surrounded by quotation marks.  Meta.
print formatter % (formatter, formatter, formatter, formatter)

# Prints the strings inside the parentheses; prints them one 
# after another, all one one line, each element (well, three 
# of the four) surrounded by # single quotation marks -- the 
# double quotation marks gone (except for the third string) --
# with a space separating each element.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
) 

# Exercise 8 Study Drills
# SD1: Do your checks of your work, write down your mistakes,
#      and try not to make them on the next exercise.
# "Your checks" is a series of checks from the ex7 Study Drills:
# (1) Write a comment on what each line does [ugh];
# (2) Read each line backward and/or aloud to find errors;
# (3) From now on, when you make a mistake, write down on paper
# what kind of mistake you made;
# (4) On the next exercise, review the mistakes you wrote down
# and try not to make them in the new exercise;
# (5) Remember, everyone makes mistakes, including programmers.

print """
Check 1 -- Add a comment about what each line does.
Done.

Check 2 -- Read each line aloud and/or backwards.
Skipped for now (no errors in output this time).

Check 3 -- Note kinds of mistakes on paper.
Will do in future.

Check 4 -- When starting next exercise, review mistakes from 
    previous exercises, and try not to do that again.
Will do in future.

Check 5 -- Remember, everyone makes mistakes, including programmers.
True dat."""

# SD2: Notice that the last line of output uses both single-
#      quotes and double-quotes for individual strings.  Why?
# The default quotation mark for strings seems to be the single-
# quote mark, and that's what's used to surround three of the
# text strings.  The third (of the four strings) is surrounded
# by double-quote marks, because the text string itself includes
# an apostrophe in the contraction "didn't", and the apostrophe
# is indistinguishable from a single quote-mark.
