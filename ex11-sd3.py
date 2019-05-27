# print "How old are you?",
# age = raw_input()
# print "How tall are you?",
# height = raw_input()
# print "How much do you weigh?",
# weight = raw_input()

# print "So, you're %r old, %r tall and %r heavy." % (
    # age, height, weight)

# Note: In Python2, "input()" has security problems, I guess because
# Python tries to interpret the input as code.  I guess "raw_input"
# doesn't though.

# Study Drills
# SD3:  Write another "form" to ask other questions.

print
fav_color = raw_input("What's your favorite color? ")
fav_song = raw_input("What's your favorite song? ")
fav_flavor = raw_input("What's your favorite ice cream flavor? ")
part1 = "So, you like the color %s, %r is your " % (
    fav_color, fav_song)
part2 = "favorite song, and you like %s ice cream." % (
    fav_flavor) 
print part1 + part2 

# That was actually harder than I expected.  I had trouble with 
# the line lengths, and resorted to putting the print strings in
# their own variables -- kind of an ugly kludge.  And it turns 
# out that formatted variables have to be on the same line as the 
# string that uses them, otherwise you get "TypeError: not all
# arguments converted during string formatting".
