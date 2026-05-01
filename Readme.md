# Grade Vault 

A simple terminal-based Python program that collects student marks, calculates averages, assigns letter grades, finds the class topper, and prints a clean report — all without using any libraries.

Built as my **second Python project** to practice loops in real use cases.

---

## What it does

- Takes input for multiple students and their subjects
- Calculates total marks and percentage for each student using loops
- Assigns a letter grade (A+ to F) based on average
- Prints a full report card for every student
- Finds the class topper by comparing averages
- Shows class-level stats: overall average, pass count, fail count

---

## Loops used

| Loop | Where |
|------|-------|
| `for` loop | Iterating over each student |
| Nested `for` loop | Collecting marks per subject |
| `for` loop | Manually calculating total marks |
| `for` loop | Printing subject-wise breakdown |
| `for` loop | Finding the topper |
| `for` loop | Calculating class average and pass/fail count |

The total marks calculation was done with a loop on purpose instead of using `sum()` — just to actually practice the concept.

---

## Sample Output

```
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
Average : 75.00%
Total   : 225 / 300
Subjects:
   Maths: 78.0
   Physics: 65.0
   Chemistry: 82.0
---------------------------------------------

Name    : Aisha
Grade   : A+
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

## How to run

Make sure you have Python 3 installed. Then:

```bash
python grade_vault.py
```

No libraries needed. Just vanilla Python.

---

## Grade Scale

| Average | Grade |
|---------|-------|
| 90 - 100 | A+ |
| 80 - 89  | A  |
| 70 - 79  | B  |
| 60 - 69  | C  |
| 50 - 59  | D  |
| Below 50 | F  |

---

## What I learned

- How `for` loops work with `range()` and with lists directly
- Nested loops for collecting multi-dimensional data
- Using a list of dictionaries to store structured data
- Manually building up logic that built-in functions could do — so the concept actually sticks
- Formatting output with f-strings and `.2f` for decimals

---



*Second project. First was a basic calculator. Trying to actually build things instead of just doing tutorials.*
