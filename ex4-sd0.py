cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = car_pool_capacity / passenger
# average_passengers_per_car = carpool_capacity / passenger
# average_passengers_per_car = carpool_capacity / passengers
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Study Drills

# SD0.  When Shaw first wrote this program, there was a typo, and the errmsg was:
# Traceback (most recent call last):
#        File "ex4.py", line 8, in <module>
#          average_passengers_per_car = car_pool_capacity / passenger
#      NameError: name 'car_pool_capacity' is not defined
#
# Explain this error, using line numbers.
#
# Shaw made a typographical error.  On line 8, he meant to type 
# the variable name "carpool_capacity" 
# but instead typed "car_pool_capacity".
# The extra underscore in the variable name meant the Python interpreter couldn't 
# find the intended variable to use when it was trying to 
# calculate "average_passengers_per_car".
#
# Interstingly, there's a second typo in line 8, also a variable name.
# The variable "passenger" is not defined.  Shaw should have typed "passengers" there.
# Line 9 is a copy of line 8, with "car_pool_capacity" changed to "carpool_capacity".
# Running it (with line 8 commented out) yields a similar error:
#
# Traceback (most recent call last):
#      File "ex4-sd.py", line 9, in <module>
#          average_passengers_per_car = carpool_capacity / passenger
#          NameError: name 'passenger' is not defined
#
# Finally, we see Shaw made another error.  Line 10 is a copy of line 8, with both
# variables names corrected.  "car_pool_capacity" is replaced by "carpool_capacity",
# and "passenger" is replaced with the correct variable name "passengers".  When we
# uncomment line 10 and run, we get that "We need to put about 1.33333333333 in each car"
# which is incorrect.  Line 11 has the corrected value:
# "average_passengers_per_car = passengers / cars_driven" which yields "about 3 in each car".

