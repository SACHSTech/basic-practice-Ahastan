'''
-------------------------------------------------------------------------------
Name:	avg_marks.py
Purpose: Calculate the 4 marks of the user

Author:	Surees.A

Created:	02/12/2020
-------------------------------------------------------------------------------
'''

# get 4 marks from the UserWarning
mark1 = float(input("Enter mark one: "))
mark2 = float(input("Enter mark two: "))
mark3 = float(input("Enter mark three: "))
mark4 = float(input("Enter mark four: "))
#compute the average of the 4 marks
marks_average = (mark1 + mark2 + mark3 + mark4)/4
# output the average
print ("The average of the four marks is: " + str(marks_average))