from grading import calculate_grade
from operations import (
    display_all_students,
    insert_student,
    remove_student,
    update_student,
)


def get_student_marks_input():
    """Helper function to prompt user for marks."""
    physics = int(input("Enter Physics Marks = "))
    chemistry = int(input("Enter Chemistry Marks = "))
    maths = int(input("Enter Maths Marks = "))
    return physics, chemistry, maths


def main():
    while True:
        print("\n...... Student Grades Management System ......")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Remove Student")
        print("4. View Students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            name = input("Enter Student Name = ")
            p_marks, c_marks, m_marks = get_student_marks_input()
            perc, grade = calculate_grade(p_marks, c_marks, m_marks)
            insert_student(name, [p_marks, c_marks, m_marks, perc, grade])

        elif choice == 2:
            name = input("Enter Student Name = ")
            p_marks, c_marks, m_marks = get_student_marks_input()
            perc, grade = calculate_grade(p_marks, c_marks, m_marks)
            update_student(name, [p_marks, c_marks, m_marks, perc, grade])

        elif choice == 3:
            name = input("Enter Student Name = ")
            remove_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("..Closing the program..")
            break

        else:
            print("Option not available. Please pick 1-5.")


if __name__ == "__main__":
    main()