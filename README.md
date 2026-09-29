# Student Grades Management System

A modular, menu-driven Python application designed to manage student academic records, calculate subject performance metrics, assign letter grades, and perform CRUD (Create, Read, Update, Delete) operations.

---

## 📁 Project Structure

The project is structured into three modular components to adhere to clean code principles and separation of concerns:

```text
student-grade-manager/
├── grading.py        # Grade calculation and percentage calculation logic
├── operations.py     # Data management module (CRUD operations)
├── main.py           # User interface and main application loop
└── README.md         # Project documentation
```

---

## 🚀 Features

- **Add Student Record:** Insert a new student entry with subject marks (Physics, Chemistry, Maths).
- **Automatic Evaluation:** Automatically calculates percentage and assigns grades (`S`, `A`, `B`, `C`, `D`, `E`, `F`).
- **Update Student Record:** Update subject marks and recalculate grade parameters for existing students.
- **Remove Student Record:** Delete student data safely from the system.
- **View All Records:** Display formatted academic summaries for all registered students.
- **Input Validation:** Handles invalid menu choices gracefully.

---

## 🛠️ Logic & Grading Scheme

Grades are determined based on the total percentage across three core subjects:

| Percentage Range | Grade | Description |
| :--- | :--- | :--- |
| $\ge 90\%$ | **S** | Outstanding |
| $80\% - 89.9\%$ | **A** | Excellent |
| $70\% - 79.9\%$ | **B** | Very Good |
| $60\% - 69.9\%$ | **C** | Good |
| $50\% - 59.9\%$ | **D** | Satisfactory |
| $31\% - 49.9\%$ | **E** | Pass |
| $\le 30\%$ | **F** | Fail |

---

## 📋 Prerequisites

- Python 3.6 or higher installed on your machine.

---

## ⚙️ How to Run

1. Clone or download all three Python files (`grading.py`, `operations.py`, and `main.py`) into the same directory.
2. Open your terminal or command prompt in that directory.
3. Execute the application with:

```bash
python main.py
```

---

## 🧪 Example Usage

```text
...... Student Grades Management System ......
1. Add Student
2. Update Student
3. Remove Student
4. View Students
5. Exit

Enter your choice: 1
Enter Student Name = Alice
Enter Physics Marks = 85
Enter Chemistry Marks = 92
Enter Maths Marks = 88
Added Alice with marks [85, 92, 88, 88.33, 'A']
```