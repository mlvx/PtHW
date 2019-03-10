# Learn Python the Hard Way [LPtHW]
# Exercise 3, Study Drill 3:  Calculate something.

print "\nCurrent weight? "; curr_weight = input()
print "Goal weight? "; goal_weight = input()
shed_weight = curr_weight - goal_weight
print "\nYou need to shed", shed_weight, "units of weight.  That's", round( shed_weight * 1.0 / curr_weight * 100 , 1) , "percent of your current weight."

