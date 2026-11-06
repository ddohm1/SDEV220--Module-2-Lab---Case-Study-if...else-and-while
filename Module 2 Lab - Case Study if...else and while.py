#Dianna Dohm
#Module 2 Lab - Case Study if...else and while.py
#This app will check to see if a student qualifies for the Dean's List or Honor's Roll
#last_name is a string that will hold input from the user containing the last name of the student or "ZZZ" if the user would like to quit
#first_name is a string that will hold input from the user containing the first name of the student
#gpa will hold input from the user containing the GPA of the student as a floating point number

print("Honor Roll and Dean's List Check!")


while True:
    last_name = input("Please enter the student's last name or type ZZZ to quit. ")
    if last_name == "ZZZ":
        break
    first_name = input("Please enter the student's first name. ")
    while True:
            try:
                gpa = float(input("Please enter the student's GPA. "))
                if gpa > 4.0 or gpa < 0.0:
                    print("Error: GPA cannot be above 4.0 or below 0.0.")
                    continue
                break
            except ValueError:
                 print("Invalid input.")   
    
    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List. ")
    if gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll ")
    if gpa < 3.25:
        print(first_name, last_name,"does not qualify for either the Dean's List or the Honor's Roll.")
   

print("Have a nice day!")

