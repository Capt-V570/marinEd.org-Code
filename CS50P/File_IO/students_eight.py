# iterating through a csv file (students.csv) with the csv library, to unpack each element of the students.csv file:
import csv

# VERSION 8 - creating a function that uses the csv library to read the csv and returns a row with student data
# to append a dictionary of data (within the list) created since version 3 (see 'students_three.py'), using fewer lines of code:

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "family": row[1]})


# this time, using a lambda (or 'anonymous function') that give it a student, is gonna simply return the name of the student
# this function will allow us to sort the list of students by taking the 'key' of the dictionary within that list and reverse the order.
for student in sorted(students, key=lambda student: student["name"]):
    print(f"Student {student['name']} is coming from {student['family']}'s Family")
