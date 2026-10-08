# Student Grade Calculator

# Get marks from the user
marks = float(input("Enter marks: "))

# Calculate the grade
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 50:
    grade = "E"
else:
    grade = "F"

# Display the grade
print("Grade:", grade)
