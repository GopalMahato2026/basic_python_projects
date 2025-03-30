#Practiceing work college's simple task again
'''
write a python program to input your percentage and the print
the grade from the following table
percentage|Grade
__________|_____
>=90      | A   
----------|-----
80-89     | B
----------|-----
50-79     | C 
----------|-----
40-49     | D
----------|-----
< 40      | F
__________|_____

'''
percentage = float(input("Enter Your Percentage: "))
#determining grades
if percentage >= 90 and percentage <= 100:
    print("Grade: A")
elif percentage < 90 and percentage >= 80:
    print("Grade: B")
elif percentage < 80 and percentage >= 50:
    print("Grade: C")
elif percentage < 50 and percentage >= 40:
    print("Grade: D")
else:
    print(f"You Failed!") 
                   