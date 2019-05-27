cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
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
SD2.  Remember that 4.0 is a "floating point" number.  What does that mean?

Reprising ex3-sd.py -- Exercise 3, Study Drill 4.  Computers use binary
numbers, not the base-ten numbers familiar to us in daily use.  In base-two,
many numbers can be represented only as approximations.  Floating-Point
Arithmetic is a technique for improving the answers we get when binary numbers
are converted back to decimal.
https://docs.python.org/2/tutorial/floatingpoint.html
https://en.wikipedia.org/wiki/Floating-point_arithmetic

For example:  Consider "0.1".  In binary, it's:
0.0001100110011001100110011001100110011001100110011...
An infinitely repeating pattern of digits is an approximation.

Consider "0.2 + 0.1".  The computer will translate each into binary, perform
the calculation which will yield a binary approximation, and convert that back
to decimal for us.

0.2 + 0.1 = 0.30000000000000004

Luckily for us, Python 2.7 and later, "Python displays a value based on the
shortest decimal fraction that rounds correctly back to the true binary value";
so for us it displays:   0.2 + 0.1 = 0.3'''

# 2019-04-16    Edited to reflect conventionally preferred style, as at:
# https://www.python.org/dev/peps/pep-0008/
