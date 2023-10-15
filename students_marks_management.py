marks_list = []
size_of_students = int(input("Enter the total lengths of students : "))

for stud in range(size_of_students):
    student_name = input("Enter the name of the student: ")
    subject_length = int(input("Enter the length of total subjects you want to add: "))
    stud_data = []
    sub_number = 1
    for data in range(subject_length):
        subject_marks = int(input(f"Enter the marks for subject {sub_number} : "))
        sub_number += 1
        stud_data.append(subject_marks)
    total_percent = sum(stud_data) / subject_length
    final_list = [student_name, stud_data, f"Total percent of student {student_name} is {total_percent}"]
    marks_list.append(final_list)

print(marks_list)
