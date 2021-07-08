'''
-------------------------------------------------------------------------------
Name:	cake_jog.py
Purpose: Find out how far the user mus jog based on how many slices of cake they had

Author:	Surees.A

Created:	02/12/2020
-------------------------------------------------------------------------------
'''
# How much cake have they eaten
calories_cake = int(input("How many pieces of cake have you eaten? "))
# total number of calories from the cake
total_calories = (calories_cake*225)
# how far they must jog
jogging_distance = (total_calories/100)
print ("To burn off the calories eaten by the cake, you must jog" , str(jogging_distance) , "km")