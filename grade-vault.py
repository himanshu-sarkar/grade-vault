# Grade Vault - Student Report Generator
# A simple python project to track student grades
# ----------------------------------------

print("=" * 45)
print("        GRADE VAULT")
print("   Student Report Generator")
print("=" * 45)

# asking how many students we want to add
num_students = int(input("\nHow many students do you want to add? "))

# this list will store all student data as dictionaries
students = []

# first loop - goes through each student one by one
for i in range(num_students):

    print(f"\n--- Student {i + 1} ---")
    name = input("Enter student name: ")

    num_subjects = int(input(f"How many subjects does {name} have? "))

    # second loop (nested) - collects marks for each subject
    subject_names = []
    marks = []

    for j in range(num_subjects):
        subject = input(f"  Subject {j + 1} name: ")
        mark = float(input(f"  Marks for {subject} (out of 100): "))

        subject_names.append(subject)
        marks.append(mark)

    # calculating total using a loop instead of just sum()
    # so it actually shows the loop logic
    total = 0
    for mark in marks:
        total = total + mark

    average = total / num_subjects

    # figuring out the letter grade based on average
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # storing everything in a dictionary and adding to the list
    student_data = {
        "name": name,
        "subjects": subject_names,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student_data)
    print(f"  ✓ {name}'s data saved!")

# ----------------------------------------
# REPORT SECTION
# ----------------------------------------

print("\n")
print("=" * 45)
print("           FINAL REPORT")
print("=" * 45)

# looping through all students to print their report
for student in students:
    print(f"\nName    : {student['name']}")
    print(f"Grade   : {student['grade']}")
    print(f"Average : {student['average']:.2f}%")
    print(f"Total   : {student['total']:.0f} / {len(student['marks']) * 100}")

    # another loop - printing each subject and its mark
    print("Subjects:")
    for k in range(len(student["subjects"])):
        subject = student["subjects"][k]
        mark = student["marks"][k]
        print(f"   {subject}: {mark}")

    print("-" * 45)

# ----------------------------------------
# FINDING THE TOPPER
# ----------------------------------------

# starting with the first student as the topper
# then looping through to check if anyone has a higher average
topper = students[0]

for student in students:
    if student["average"] > topper["average"]:
        topper = student

print(f"\n Class Topper : {topper['name']}")
print(f"   Average Score : {topper['average']:.2f}%")
print(f"   Grade         : {topper['grade']}")

# ----------------------------------------
# SUMMARY STATS
# ----------------------------------------

print("\n--- Class Summary ---")

# calculating class average using a loop
total_class_marks = 0
for student in students:
    total_class_marks = total_class_marks + student["average"]

class_average = total_class_marks / len(students)
print(f"Class Average : {class_average:.2f}%")

# counting how many students passed and failed
passed = 0
failed = 0

for student in students:
    if student["average"] >= 50:
        passed = passed + 1
    else:
        failed = failed + 1

print(f"Passed        : {passed} student(s)")
print(f"Failed        : {failed} student(s)")

print("\n" + "=" * 45)
print("         End of Report")
print("=" * 45)
