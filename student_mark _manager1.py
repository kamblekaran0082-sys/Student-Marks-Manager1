
# Student Marks Manager
# This program takes a student's marks and calculates their result.

# Get student's name
name = input("Enter student name: ")


# Get Python marks with basic input validation
while True:
    try:
        mark1 = int(input("Enter Python mark: "))
        break

    except ValueError:
        print("Please enter valid marks.")


# Get SQL marks with basic input validation
while True:
    try:
        mark2 = int(input("Enter SQL mark: "))
        break

    except ValueError:
        print("Please enter valid marks.")


# Get ML marks with basic input validation
while True:
    try:
        mark3 = int(input("Enter ML mark: "))
        break

    except ValueError:
        print("Please enter valid marks.")


# Store student information in a dictionary
student = {
    "name": name,
    "age": 21,
    "course": "BSc CS",
    "marks": [mark1, mark2, mark3]
}


# Calculate total, average, result, grade, highest and lowest marks
def calculate_result(marks):

    total = sum(marks)
    average = total / len(marks)

    # Check whether the student passed or failed
    if average >= 40:
        result = "Pass"
    else:
        result = "Fail"

    # Calculate grade based on average marks
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    # Find highest and lowest marks
    highest = max(marks)
    lowest = min(marks)

    return total, average, result, grade, highest, lowest


# Call the function and store the returned values
total, average, result, grade, highest, lowest = calculate_result(
    student["marks"]
)


# Display the student's result
print("Student:", student["name"])
print("Python:", mark1)
print("SQL:", mark2)
print("ML:", mark3)
print("Total:", total)
print("Average:", round(average, 2))
print("Result:", result)
print("Grade:", grade)
print("Highest:", highest)
print("Lowest:", lowest)

