students_marks={ }

def insert_students(name,marks):
    students_marks[name]= marks
    print("added",name , "with marks", marks)

def update_students(name,marks):
        if name in students_marks:
            students_marks[name]=marks
            print( name,"updated with marks",marks)

        else:
            print(name," not found!")    

def remove_students(name):
    if name in students_marks:
        del students_marks[name]
        print(name," is removed successfully")

    else:
        print(name," not found!")

def display_all_students():
    if students_marks: 
        for name, marks in students_marks.items():
            print( name," : ", marks)
    else:
        print("student no found")

def main():
    while True:
        print(" ...... Student Grades Management System ......" )
        print("1. Add Student")
        print("2. Update Student")
        print("3. Remove Student")
        print("4. View Student")
        print("5. Exit")

        choose=int(input(" Enter your choice:"))
        if choose==1:
            name=input("Enter Student=")
            Pmarks=int(input("Enter Student Physics Marks="))
            Cmarks=int(input("Enter Student Chemistry Marks="))
            Mmarks=int(input("Enter Student Maths Marks="))
            perc= (Pmarks+Cmarks+Mmarks)/3
            if perc>=90:
                Grade="S"
            elif perc>=80:
                Grade="A"
            elif perc>=70:
                Grade="B"
            elif perc>=60:
                Grade="C"
            elif perc>=50:
                Grade="D"
            elif perc<=30:
                Grade="F"
            else:
                Grade="E"
            insert_students(name,[Pmarks,Cmarks,Mmarks,perc,Grade])

        elif choose==2:
            name=input("Enter Student=")
            Pmarks=int(input("Enter Student Physics Marks="))
            Cmarks=int(input("Enter Student Chemistry Marks="))
            Mmarks=int(input("Enter Student Maths Marks="))
            perc= (Pmarks+Cmarks+Mmarks)/3
            if perc>=90:
                Grade="S"
            elif perc>=80:
                Grade="A"
            elif perc>=70:
                Grade="B"
            elif perc>=60:
                Grade="C"
            elif perc>=50:
                Grade="D"
            elif perc<=30:
                Grade="F"
            else:
                Grade="E"
            update_students(name,[Pmarks,Cmarks,Mmarks,perc,Grade])

        elif choose==3:
            name=input("Enter Student=")
            remove_students(name)

        elif choose==4:
            display_all_students()

        elif choose==5:  
            return ("..Closing the program..")
            break   

        else:
            print("Not Available")
print(main())