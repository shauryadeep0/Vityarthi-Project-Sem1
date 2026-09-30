# Student Grades Management System

## Overview

A simple Python command-line application for managing student marks and grades. Users can add, update, remove, and view student records.

## Features

*  Add student records
*  Update student marks
*  Remove students
*  View all students
*  Calculate percentage
*  Automatically assign grades
*  Exit the program

## Technologies / Tools

* **Python 3**
* **Dictionary** – Stores student records
* **Command-line interface** – Used for interaction

## Installation

1. Install Python 3.
2. Download or clone the project.
3. Open the project directory.

No external libraries are required.

## Running the Project
Install colorama:

```bash
pip install colorama
```

Run:

```bash
python main.py
```

Replace `main.py` with the actual filename if different.

## How to Use

Choose an option from the menu:

1. **Add Student** – Enter the student's name and marks in Physics, Chemistry, and Maths.
2. **Update Student** – Modify the marks of an existing student.
3. **Remove Student** – Delete a student record.
4. **View Student** – Display all stored student records.
5. **Exit** – Close the program.

The system calculates the average percentage and assigns a grade automatically.

## Testing

Test the following:

* Adding a new student.
* Updating an existing student.
* Updating a student who does not exist.
* Removing a student.
* Removing a student who does not exist.
* Viewing student records.
* Different marks and grade ranges.
* Invalid menu choices.

## Future Improvements

* Input validation for marks.
* Search for individual students.
* Calculate class average.
* Sort students by marks.
* Save records permanently using a file or database.
* Improve the user interface.

## License

Educational project created for learning Python programming.
