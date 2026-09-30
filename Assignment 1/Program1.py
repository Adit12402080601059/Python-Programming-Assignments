# Student Record Management

n, k, m = map(int, input().split())

students = []
semesters = {}

# Taking student details
for i in range(n):
    data = input().split()

    enrollment = data[0]
    name = data[1]
    semester = int(data[2])
    cpi = float(data[3])

    marks = []
    for j in range(m):
        marks.append(int(data[4 + j]))

    # Tuple containing student information
    student = (enrollment, name, semester, cpi, marks)

    # Store in list
    students.append(student)

    # Store students semester-wise in dictionary
    if semester not in semesters:
        semesters[semester] = []

    semesters[semester].append(student)


# Print Top K students semester-wise
for semester in sorted(semesters.keys()):

    student_list = semesters[semester]

    # Sort according to:
    # 1. Higher CPI
    # 2. Higher average marks
    # 3. Smaller enrollment number

    student_list.sort(
        key=lambda x: (
            -x[3],
            -sum(x[4]) / m,
            x[0]
        )
    )

    print("Semester", semester, end=": ")

    for i in range(min(k, len(student_list))):
        print(student_list[i][0], end=" ")

    print()


# Find subject-wise toppers
for subject in range(m):

    highest = -1
    toppers = []

    for student in students:

        enrollment = student[0]
        marks = student[4]

        if marks[subject] > highest:
            highest = marks[subject]
            toppers = [enrollment]

        elif marks[subject] == highest:
            toppers.append(enrollment)

    toppers.sort()

    print("S" + str(subject + 1) + ":", end=" ")

    for enrollment in toppers:
        print(enrollment, end=" ")

    print()
