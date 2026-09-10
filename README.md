# CLI Grade Calculator

A simple and interactive Command Line Interface (CLI) Grade Calculator built in Python. This project takes marks input for multiple subjects from the user, calculates total percentage, and assigns the corresponding overall letter grade.

## Features

- **Dynamic Subject Input:** Accepts marks for any number of user-defined subjects.
- **Strict Input Validation:** Handles invalid numbers, negative inputs, marks exceeding 100, and non-integer/string errors gracefully without crashing.
- **Structured Data Storage:** Utilizes Python dictionaries to map subject names to their respective marks.
- **Automatic Calculation:** Calculates total marks, max achievable marks, percentage, and letter grade automatically using custom logic.
- **Clean CLI Output:** Displays a formatted grade report directly in the terminal.

## Core Concepts Covered

This project demonstrates core Python fundamentals:
- **Functions:** Modular function definitions (`calculate_grade` and `main`).
- **Loops:** `while` loops for input validation and `for` loops for iterating over subjects and dictionaries.
- **Dictionaries:** Key-value mapping for storing subject names and corresponding scores.
- **Exception Handling:** `try-except` blocks for handling `ValueError` on bad inputs.

## Grade Calculation Logic

| Percentage Range | Grade |
| :--- | :--- |
| **90% - 100%** | A+ |
| **80% - 89%** | A |
| **70% - 79%** | B |
| **60% - 69%** | C |
| **50% - 59%** | D |
| **Below 50%** | F |

## Sample Output

```text
=== CLI Grade Calculator ===
Enter total number of subjects: 3
Enter name for subject 1: Maths
Enter marks obtained in Maths (0-100): 85
Enter name for subject 2: Science
Enter marks obtained in Science (0-100): 92
Enter name for subject 3: English
Enter marks obtained in English (0-100): 78

==============================
        GRADE REPORT        
==============================
Maths          : 85.00
Science        : 92.00
English        : 78.00
------------------------------
Total Marks    : 255.00 / 300
Percentage     : 85.00%
Overall Grade  : A
==============================
