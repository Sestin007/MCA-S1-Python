# c) Write a Python program to maintain student records using a dictionary where:
#    i. Keys are student names.
#    ii. Values are lists of marks in 3 subjects.
#    Calculate the total marks and average marks.

students = {
    "Anu": [85, 90, 78],
    "Gowri": [72, 88, 91],
    "Vishnu": [95, 80, 85]
}
for name, marks in students.items():
    total = sum(marks)                  
    average = sum(marks) / len(marks)   
    print("\nStudent:", name)
    print("Marks:", marks)
    print("Total Marks:", total)
    print("Average Marks:", f"{average:.2f}")
    print("." * 20)