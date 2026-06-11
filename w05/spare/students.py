import csv

index_id=0
index_first_name=1
index_last_name=2
index_sex=3
index_email=5
index_age=4


def main():
    print("n\Hello !!")

    id=int(input("enter an id: "))
    first_name=input("Enter your first name: ")
    last_name=input("Enter your last name: ")
    sex=input("Enter your sex: ")
    age=int(input("Enter your age: "))
    email=input("Enter your email: ")
    

    with open("w05/students.csv", "a", newline="") as file:
        students=csv.writer(file)
        students.writerow([id,first_name,last_name,sex,age,email])
    with open("w05/students.csv", "rt") as file:
        students=csv.reader(file)
        next(students)
        for i in students:
            ids=i[index_id]
            print(ids)

    
       

 






if __name__ == "__main__":
    main()