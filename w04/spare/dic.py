
INDEX_FIRST_NAME=0
INDEX_LASTNAME=1
INDEX_SEX=2
INDEX_AGE=3



def main():
#declaring menus list
    menus=[
        "Add a student", "Delete a student",
        "Edit student information", "Add grades for each course",
        "Calculate the overall average", "Display all students",
        "Search for a student by ID", "Sort students by average",
        "Save data into a file", "Load data from a file", "Exit"
           ]
    
    students={

    }
    
    #displaying manus to user and getting a value from him
    for i, j in enumerate(menus):
        print(f"{i+1}. {j}")
    userinput=get_digit_number("Choose one of them: ")
    while userinput != 11:
        if userinput < 1 or userinput > 11:
            print("Please enter a number between 1 to 11.")
        if userinput==1:
            print("please fill out this form")
            id=get_digit_number("Student ID: ")
            first_name=input("First Name: ").upper()
            last_name=input("Last Name: ").upper()
            sex=input("Sex: ").upper()
            age=get_digit_number("Age: ")

            students[id]={
                "First Name":first_name,
                "Last nam":last_name,
                "Sex":sex,
                "Age":[age, "years old"]
            }
            vertically_displayed(students)
            for i, j in enumerate(menus):
                print(f"{i+1}. {j}")
        elif userinput==2:
            print("\nHere is the database: ")
            vertically_displayed(students)
            delete_student(students)
            for i, j in enumerate(menus):
                print(f"{i+1}. {j}")









        # Handle valid choices
        elif userinput == 3:
            print("be patient brother 😂")
        elif userinput == 4:
            print("Deleting a student... (Feature coming soon)")
        # You can add elif blocks for options 3 through 10 here
        
        # CRITICAL FIX: Ask for input again so the loop doesn't get stuck infinitely!
        userinput = get_digit_number("\nChoose one of them: ")

    print("Goodbye!")

        


#getting only a digit number     
def get_digit_number(prompt):
    result=input(prompt)
    while not result.isdigit():
        print("Please enter a digit number not a string")
        result=input(prompt)
    result=int(result)
    return result      
#display student dictionary vertically
def vertically_displayed(students_dictionary):
    if len(students_dictionary)==0:
        print("No data found")
        print()
    else:
        for id, info in students_dictionary.items(): 
            print()      
            print(f"id: {id}")
            for key, value in info.items():
                print(key, ":", value)
                print()
                
def delete_student(student_dictionary):
    delid=get_digit_number("enter student ID: ")
    if delid in student_dictionary:
        del student_dictionary[delid]
        print(f"student from this {delid} has been deleted")
    else:
        print("\nstudent not found")
        print()















# Call the main function to run the program
if __name__ == "__main__":
    main()    
