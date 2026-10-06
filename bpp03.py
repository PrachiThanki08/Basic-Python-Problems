name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))

percentage = (m1 + m2 + m3) / 3

print("Student Name:", name)
print("Roll Number:", roll_no)
print("Percentage:", percentage)

marks = {
    "Subject 1": m1,
    "Subject 2": m2,
    "Subject 3": m3
}

highest = max(marks, key=marks.get)
lowest = min(marks, key=marks.get)

print("Highest Marks:", highest, marks[highest])
print("Lowest Marks:", lowest, marks[lowest])