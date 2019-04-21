from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)

# Study Drills

# SD1:  Find out what Zork and Adventure where.  Find and play a copy.
# I still remember trying to play Adventure.  It was a text-based game where
# you played by typing things like "go east", "grab sword", or "kill orc".
# If you typed  something the computer was not programmed to recognize, it
# would say "I  don't know how to do that" or "not recognized".  I never got
# very far in the game, but I know it was popular.  Wikipedia makes me think
# the full name was "Colossal Cave Adventure", and it was the earliest known
# example of the "interactive fiction" game genre.
# Wikipedia says Zork was a similar game, originally written in MDL and 
# running on a PDP-10.  Apparently, Zork was published commercially in three
# parts; and was considered an especially rich example of the genre, with a
# sophisticated text parser.
