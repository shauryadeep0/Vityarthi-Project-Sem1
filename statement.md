# Problem Statement & System Architecture

## 1. Problem Statement

Educational institutions and educators often struggle with managing student academic data efficiently using manual or unorganized systems. Keeping track of individual marks across multiple subjects, calculating overall percentages, and manually assigning grades can lead to human error, inconsistency, and inefficiency.

### Objectives
- Build a structured, command-line interface (CLI) software program to handle student records.
- Automate percentage calculations and letter grade assignments based on subject inputs.
- Ensure modular code architecture by decoupling data persistence, calculation algorithms, and user interaction.
- Offer an intuitive user experience with easy menu navigation and data entry error handling.

---

## 2. System Architecture & Component Design

The application follows a modular separation of concerns pattern:

### A. Core Components

1. **`grading.py` (Domain Logic):**
   - **Responsibility:** Contains standalone functions for math calculations and grading metrics.
   - **Function:** `calculate_grade(physics, chemistry, maths)`
     - Input: Individual numerical marks.
     - Output: Tuple `(percentage, grade)`.

2. **`operations.py` (Data Access Layer):**
   - **Responsibility:** Operates on the underlying data store (`students_marks` dictionary).
   - **Functions:** 
     - `insert_student(name, marks)`
     - `update_student(name, marks)`
     - `remove_student(name)`
     - `display_all_students()`

3. **`main.py` (Presentation & Orchestration Layer):**
   - **Responsibility:** Manages CLI execution, captures user input, validates options, and connects UI interactions with underlying modules.

---

## 3. Mathematical & Algorithmic Design

Let $P$, $C$, and $M$ denote the marks obtained in Physics, Chemistry, and Mathematics respectively.

The aggregate percentage $Perc$ is calculated as:

$$\text{Perc} = \frac{P + C + M}{3}$$

The letter grade $G$ is governed by the piecewise function:

$$
G(Perc) = 
\begin{cases} 
\text{S} & \text{if } Perc \ge 90 \\
\text{A} & \text{if } 80 \le Perc < 90 \\
\text{B} & \text{if } 70 \le Perc < 80 \\
\text{C} & \text{if } 60 \le Perc < 70 \\
\text{D} & \text{if } 50 \le Perc < 60 \\
\text{F} & \text{if } Perc \le 30 \\
\text{E} & \text{otherwise}
\end{cases}
$$