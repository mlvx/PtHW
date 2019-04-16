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

# SD0.	When Shaw first wrote this program, there was a typo.  Errmsg was...
# See file ex4-sd0.py.

# SD1.	Shaw used "4.0" for var. "space_in_a_car".  Is that necessary?  What 
#	happens if it were simply "4"?
# Var. "space_in_a_car" is defined in line 2, and used in line 7 to calculate
# the var.  # "carpool_capacity".  Defining it at 4.0 makes it a floating point
# number (aka # "float"), which is not necessary for the "carpool_capacity"
# calculation, because the # calculation is a multiplication.  (It *would*
# be necessary if the calculation were a # division.)

# 2019-04-16	Edited to reflect conventionally preferred style, as at:
# https://www.python.org/dev/peps/pep-0008/
