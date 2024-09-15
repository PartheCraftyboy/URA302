class Student:
    def __init__(self, student_id, student_name, student_class = "Ist year"):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display_attributes(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Class: {self.student_class}")

# Example usage
student1 = Student(student_id=101, student_name='Alice')
student1.display_attributes()