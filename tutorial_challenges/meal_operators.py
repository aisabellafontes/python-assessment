"""
Task 
Given the meal price (base cost of a meal), 
tip percent (the percentage of the meal price being added as tip), 
and tax percent (the percentage of the meal price being added as tax) 
for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, 
or you may end up with an incorrectly rounded result!

Sample Input

12.00
20
8

Sample Output

The total meal cost is 15 dollars.

Explanation

totalCost = mealCost + tip + taxi
tip = the percentage of mealCost being added as tip
taxi = the percentage of mealCost being added as tax

Challenge solving by @aisabellafontes

"""
def operators_manual(mealCost, tipCost, taxiCost):
    totalCost = mealCost + (mealCost*(tipCost/100)) + (mealCost*(taxiCost/100))
    return round(totalCost)

def operators(mealCost, L):
    return round(mealCost + sum(map(lambda x: mealCost*(x/100), L)))

mealCost = float(raw_input())
tipCost = float(raw_input())
taxiCost = float(raw_input())

print "Iteration: The total meal cost is {0} dollars.".format(int(operators(mealCost, [tipCost, taxiCost])))
print "Manual: The total meal cost is {0} dollars.".format(operators_manual(mealCost, tipCost, taxiCost))

