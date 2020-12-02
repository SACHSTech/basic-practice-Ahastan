'''
-------------------------------------------------------------------------------
Name: oz_to_ml.py
Purpose: Find out how many mL of fluid the user must need based on the anount of fluid (ounces) and the amount of people being served.

Author:	Surees.A

Created:	02/12/2020
-------------------------------------------------------------------------------
'''
# get the amount of ounces
fluid_ounces = float(input("Enter the amount of fluid in ounces: "))
# get the amount of people to serve
people = int(input("Enter the number of people to serve: "))
# convert ounces to milliliters
mL_of_fluid = (fluid_ounces*29.574)
# total mL
total = (mL_of_fluid*people)
print ("")
print ("You will need " + str(total) , "ml")