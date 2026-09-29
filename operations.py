# Shared dictionary to store student records
students_marks = {}


def insert_student(name, marks):
    students_marks[name] = marks
    print(f"Added {name} with marks {marks}")


def update_student(name, marks):
    if name in students_marks:
        students_marks[name] = marks
        print(f"{name} updated with marks {marks}")
    else:
        print(f"{name} not found!")


def remove_student(name):
    if name in students_marks:
        del students_marks[name]
        print(f"{name} removed successfully")
    else:
        print(f"{name} not found!")


def display_all_students():
    if students_marks:
        print("\n--- Current Student Records ---")
        for name, data in students_marks.items():
            physics, chemistry, maths, perc, grade = data
            print(
                f"{name} -> Physics: {physics}, Chemistry: {chemistry}, "
                f"Maths: {maths} | Percentage: {perc}% | Grade: {grade}"
            )
    else:
        print("No student records found.")