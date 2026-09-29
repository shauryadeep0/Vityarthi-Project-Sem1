from colorama import init, Fore, Style

# Initialize colorama with autoreset
init(autoreset=True)

students_marks = {}

def insert_students(name, marks):
    students_marks[name] = marks
    print(Fore.GREEN + "added", name, "with marks", marks)

def update_students(name, marks):
    if name in students_marks:
        students_marks[name] = marks
        print(Fore.GREEN + name, "updated with marks", marks)
    else:
        print(Fore.RED + name, "not found!")    

def remove_students(name):
    if name in students_marks:
        del students_marks[name]
        print(Fore.GREEN + name, "is removed successfully")
    else:
        print(Fore.RED + name, "not found!")

def display_all_students():
    if students_marks: 
        for name, marks in students_marks.items():
            print(Fore.CYAN + name, ":", marks)
    else:
        print(Fore.RED + "student not found")

def main():
    while True:
        print(Fore.YELLOW + Style.BRIGHT + " ...... Student Grades Management System ......" )
        print(Fore.CYAN + "1. Add Student")
        print(Fore.CYAN + "2. Update Student")
        print(Fore.CYAN + "3. Remove Student")
        print(Fore.CYAN + "4. View Student")
        print(Fore.CYAN + "5. Exit")

        try:
            choose = int(input(" Enter your choice:"))
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")
            continue

        if choose == 1:
            name = input("Enter Student=")
            Pmarks = int(input("Enter Student Physics Marks="))
            Cmarks = int(input("Enter Student Chemistry Marks="))
            Mmarks = int(input("Enter Student Maths Marks="))
            perc = (Pmarks + Cmarks + Mmarks) / 3
            
            if perc >= 90:
                Grade = "S"
            elif perc >= 80:
                Grade = "A"
            elif perc >= 70:
                Grade = "B"
            elif perc >= 60:
                Grade = "C"
            elif perc >= 50:
                Grade = "D"
            elif perc <= 30:
                Grade = "F"
            else:
                Grade = "E"
            
            insert_students(name, [Pmarks, Cmarks, Mmarks, perc, Grade])

        elif choose == 2:
            name = input("Enter Student=")
            Pmarks = int(input("Enter Student Physics Marks="))
            Cmarks = int(input("Enter Student Chemistry Marks="))
            Mmarks = int(input("Enter Student Maths Marks="))
            perc = (Pmarks + Cmarks + Mmarks) / 3
            
            if perc >= 90:
                Grade = "S"
            elif perc >= 80:
                Grade = "A"
            elif perc >= 70:
                Grade = "B"
            elif perc >= 60:
                Grade = "C"
            elif perc >= 50:
                Grade = "D"
            elif perc <= 30:
                Grade = "F"
            else:
                Grade = "E"
                
            update_students(name, [Pmarks, Cmarks, Mmarks, perc, Grade])

        elif choose == 3:
            name = input("Enter Student=")
            remove_students(name)

        elif choose == 4:
            display_all_students()

        elif choose == 5:  
            return Fore.MAGENTA + "..Closing the program.."

        else:
            print(Fore.RED + "Not Available")

print(main())