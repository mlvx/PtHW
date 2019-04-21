from sys import argv

script, user_name, clan = argv
prompt = 'Type-Input-Here:_'

print "Hi %s of Clan %s, I'm the %s script." % (
    user_name, clan, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "Where does Clan %s come from?" % clan
origin = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r, and Clan %r is from %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, clan, origin, computer) 

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
# Windows Subsystem for Linux includes a version of Adventure.  Started
# playing.  A dwarf threw an axe at me.  I got 54 points out of possible 350.
# If / when I resume, it's "adven_2019-0421".

# SD2:  Change the  prompt  variable to something else entirely.
# Done.  Trivial; but it's nice to change in one place, and have it work
# everywhere.  The power of variables.

# SD3:  Add another argument and use it in your script.
# Done.

# SD4:  Make sure you understand combining """ multi-line strings with the %
# format 'activator' as the last print.
# That's actually kind of slick.  The  %  operator and the opening paren have
# to be on the same line as the closing quotemark; but if the line is getting
# long, then you can put the arguments on the next line.  Indentation is
# optional, but good style for readability.
