import pandas as pd

students = pd.DataFrame({
    "id":[1,2,3,4],
    "name":["John","Sara","Mike","Lisa"],
    "dept":["CS","IT","CS","EC"],
    "marks":[80,90,75,85]
})

departments = pd.DataFrame({
    "dept":["CS","IT","EC"],
    "dept_name":["Computer Science","Information Tech","Electronics"]
})
proj_students = students[["name","marks"]]
print("PROJECT (name, marks):")
print(proj_students, "\n")
high_scorers = students[students["marks"] > 80]
print("FILTER (marks > 80):")
print(high_scorers, "\n")
sorted_students = students.sort_values("marks", ascending=False)
print("SORTED (by marks DESC):")
print(sorted_students, "\n")
avg_marks = students.groupby("dept")["marks"].mean().reset_index()
print("GROUP + AVG(marks) by dept:")
print(avg_marks, "\n")
student_with_dept = pd.merge(students, departments, on="dept")
print("JOIN (students with departments):")
print(student_with_dept, "\n")


