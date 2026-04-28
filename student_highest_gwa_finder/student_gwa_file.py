class Student:
    def __init__(self, name, gwa):
        self.name = name
        self.gwa = float(gwa)
class StudentFileHandler:
    def __init__(self, filename):
        self.filename = filename
    def read_students(self):
        students = []
        with open(self.filename) as file:
            for line in file:
                name, gwa = line.strip().split(",")
                students.append(Student(name, gwa))
        return students
    def find_highest_gwa(self, students):
        highest = students[0]
        for student in students:
            if student.gwa > highest.gwa:
                highest = student
        return highest
# main
handler = StudentFileHandler("students.txt")
students = handler.read_students()
top_student = handler.find_highest_gwa(students)
print("highest gwa student:")
print(top_student.name, "=", top_student.gwa)