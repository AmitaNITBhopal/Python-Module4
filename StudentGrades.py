studentGrades = {}

choice = 5
while(choice != 4):
    print("\nMenu \n Please select one option")
    print("\n 1. Add Student\n 2. Update Student\n 3. Print all Student's grades\n 4. Exit\n")
    choice = int(input())
    if(choice == 1) :
        name = input("Enter the new Student name\n")
        grade = input("Enter his/her grade\n")
        studentGrades[name] = grade

    elif(choice == 2) :
        name = input("Enter the Student name\n")
        if(studentGrades.get(name) == None) :
            print("This student does not exist, please select another option from menu")
        else :
            grade = input("Enter the new grade\n")
            studentGrades[name] = grade

    elif(choice == 3) :
        print("Existing Students and their Grades are :\n")
        print(studentGrades)

    elif(choice == 4) :
        print("Thank you, Bye!\n")

    else :
        print("Please select as per menu\n")
