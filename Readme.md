# Grade Vault 

A simple terminal-based Python program that collects student marks, calculates averages, assigns letter grades, finds the class topper, and prints a clean report card.

Built as my **second Python project** to practice loops, nested loops, lists, dictionaries, and report generation logic in a practical way.

---

## What it does

- Takes input for multiple students and their subjects
- Calculates total marks and percentage for each student using loops
- Assigns a letter grade (A+ to F) based on average
- Generates performance remarks based on scores
- Prints a detailed report card for every student
- Finds the class topper by comparing averages
- Shows class-level stats:
  - overall class average
  - pass count
  - fail count

---

## Loops used

| Loop | Where |
|------|-------|
| `for` loop | Iterating over each student |
| Nested `for` loop | Collecting subject names and marks |
| `for` loop | Manually calculating total marks |
| `for` loop | Printing subject-wise marks |
| `for` loop | Finding the class topper |
| `for` loop | Calculating class average |
| `for` loop | Counting passed and failed students |

The total marks calculation was intentionally done using loops instead of `sum()` to practice loop logic properly.

---

## Features Included

- Multiple student support
- Multiple subject support
- Average percentage calculation
- Grade assignment
- Performance remarks
- Subject-wise report display
- Class topper detection
- Class summary statistics
- Clean terminal formatting

---

## Sample Output

```text
=============================================
        GRADE VAULT
   Student Report Generator
=============================================

How many students do you want to add? 2

--- Student 1 ---
Enter student name: Rohan
How many subjects does Rohan have? 3
  Subject 1 name: Maths
  Marks for Maths (out of 100): 78
  Subject 2 name: Physics
  Marks for Physics (out of 100): 65
  Subject 3 name: Chemistry
  Marks for Chemistry (out of 100): 82
  ✓ Rohan's data saved!

--- Student 2 ---
Enter student name: Aisha
How many subjects does Aisha have? 3
  Subject 1 name: Maths
  Marks for Maths (out of 100): 91
  Subject 2 name: Physics
  Marks for Physics (out of 100): 88
  Subject 3 name: Chemistry
  Marks for Chemistry (out of 100): 94
  ✓ Aisha's data saved!

=============================================
           FINAL REPORT
=============================================

Name    : Rohan
Grade   : B
Remark  : Very good work!
Average : 75.00%
Total   : 225 / 300
Subjects:
   Maths: 78.0
   Physics: 65.0
   Chemistry: 82.0
---------------------------------------------

Name    : Aisha
Grade   : A+
Remark  : Outstanding performance!
Average : 91.00%
Total   : 273 / 300
Subjects:
   Maths: 91.0
   Physics: 88.0
   Chemistry: 94.0
---------------------------------------------

🏆 Class Topper : Aisha
   Average Score : 91.00%
   Grade         : A+

--- Class Summary ---
Class Average : 83.00%
Passed        : 2 student(s)
Failed        : 0 student(s)

=============================================
         End of Report
=============================================
```

---

## How to Run

Make sure Python 3 is installed.

Run the project using:

```bash
python grade_vault.py
```

No external libraries required.

---

## Grade Scale

| Average | Grade |
|---------|-------|
| 90 - 100 | A+ |
| 80 - 89  | A |
| 70 - 79  | B |
| 60 - 69  | C |
| 50 - 59  | D |
| Below 50 | F |

---

## What I Learned

- Using `for` loops with `range()`
- Nested loops for structured input collection
- Working with lists and dictionaries together
- Building manual logic instead of relying on built-in shortcuts
- Formatting clean terminal output using f-strings
- Organizing data using dictionaries inside lists
- Basic report generation logic in Python

---
