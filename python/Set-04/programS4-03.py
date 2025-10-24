students = { "Anu": [85, 90, 78], "Gowri": [72, 88, 91], "Vishnu": [95, 80, 85] }

# Display student records
for name, marks in students.items():
    total = sum(marks) # total marks
    average = sum(marks) / len(marks) # average marks
    print(f"Student: {name}")
    print(f"Marks: {marks}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print("." * 20)
