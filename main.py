import json
import os

# defines constants
NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]
DIRECTORY = "students/"

# retuns json report card as dict
def load_report_card(directory: str, student_number: int):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card

# returns the average grade for the student
def get_average_grade(report_card: dict, subjects: list):
    all_grades = 0
    for subject in subjects:
        all_grades += report_card[subject]

    return all_grades / len(subjects)

# returns the student's easiest/hardest subject
def easiest_hardest_grade(report_card: dict, subjects: list):
    info = {"easiest":"math", "hardest":"math"}
    for subject in subjects:
        if report_card[subject] > report_card[info["easiest"]]:
            info["easiest"] = subject
        if report_card[subject] < report_card[info["hardest"]]:
            info["hardest"] = subject

    return info["easiest"], info["hardest"]

# returns a dict with the sum of all grades for each subject
def addto_sum_all_grades(report_card: dict, sum_all_grades: dict, subjects: list) :
    for subject in subjects:
        sum_all_grades[subject] += report_card[subject]

    return sum_all_grades


# data to be worked with/manipulated
all_averages = []
sum_all_grades = {"math": 0 , "science": 0, "history": 0, "english": 0, "geography": 0}
avg_all_grades = {"math": 0 , "science": 0, "history": 0, "english": 0, "geography": 0}

# format - {grade_level : [total_grade, count]}
all_grade_levels = {i : [0,0] for i in range(1,9)}

# tuples to compare students with
best_student = (0, 0)
worst_student = (0, 100)

# iterates through all students
for i in range(NUM_STUDENTS):
    report_card = load_report_card(DIRECTORY, i)
    card_average = get_average_grade(report_card, SUBJECTS)

    all_averages.append(card_average)
    sum_all_grades = addto_sum_all_grades(report_card, sum_all_grades, SUBJECTS)
    
    all_grade_levels[report_card["grade"]][0] += card_average
    all_grade_levels[report_card["grade"]][1] += 1

    if card_average > best_student[1]:
        best_student = (report_card["id"], card_average)
    if card_average < worst_student[1]:
        worst_student = (report_card["id"], card_average)


# retuns average of all grades in each subject
for subject in avg_all_grades:
    avg_all_grades[subject] = sum_all_grades[subject] / 1000


# prints all relevant information
print(f"Average Student Grade: {sum(all_averages) / len(all_averages):.2f}")
print(f"Hardest Subject: {min(avg_all_grades, key=lambda x: avg_all_grades[x])}")
print(f"Easiest Subject: {max(avg_all_grades, key=lambda x: avg_all_grades[x])}")
print(f"Best Performing Grade: {max(all_grade_levels, key=lambda x: all_grade_levels[x][0] / all_grade_levels[x][1])}")
print(f"Best Performing Grade: {min(all_grade_levels, key=lambda x: all_grade_levels[x][0] / all_grade_levels[x][1])}")
print(f"Best Student ID: {best_student[0]}")
print(f"Worst Student ID: {worst_student[0]}")