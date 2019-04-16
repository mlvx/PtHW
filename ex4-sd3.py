# Straightforward numerical assignment.
cars = 100
# Straightforward numerical assignment.
space_in_a_car = 4.0
# Straightforward numerical assignment.
drivers = 30
# Straightforward numerical assignment.
# passengers = 90
passengers = 89.0

# Defines new var., assigns value by calculation, using two previously defined
# and assigned vars.
cars_not_driven = cars - drivers

# Defines "cars_driven" to be the same as "drivers".  Interesting, because
# we could use "drivers" instead of defining a new variable.  I wonder about
# the advantages of each approach, when later maintaining code.
cars_driven = drivers

# Defines new var., assigns value by calculation, using two previously defined
# and assigned vars.  
carpool_capacity = cars_driven * space_in_a_car

# Defines new var., assigns value by calculation, using two previously defined
# and assigned vars.  In this instance, a division calculation, the previous
# assignment choices (integer or floating-point) can have an effect on the
# number that is displayed.  90 / 30 = 3 ; but suppose "passengers" had a value
# of, say, 89?  That would lead to "We need to put about 2 in each car".  If
# "passengers" has value "89.0", we get "We need to put about 2.96666666667 in
# each car".  (WTH is .966667 of a passenger?  Chop off a finger??)  So, the
# sensible way to do this would be:  Assign the variable as a floating point;
# perform the calculation; round the answer to something that makes sense to
# a human.
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Study Drills

# SD1.  Is it necessary to use "4.0" for the var. "space_in_a_car"?
# No, because it's used in a multiplication, not a division (line 7).

print '''
SD3.  Write comments above each of the variable assignments.
Um... Why?  Ok, I'll do it.
Ok, that was more interesting than I expected.

SD4.  Make sure you know what "=" is called (equals), and that it's
	making names for things.
Ok.  (Not making a new file for that.)

SD5.  Remember that "_" is an underscore character.
Ok.  (Not making a new file for that either.)
'''

# 2019-04-16	Edited to reflect conventionally preferred style, as at:
# https://www.python.org/dev/peps/pep-0008/
