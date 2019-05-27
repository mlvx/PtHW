print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# Study Drills
# SD2:  Find and try out other ways to use "raw_input".
# The most obvious way is with a prompt.

print
fav_num = raw_input("What's your favorite number? ")
fav_num = float(fav_num)
print "The square of your favorite number is", fav_num * fav_num


