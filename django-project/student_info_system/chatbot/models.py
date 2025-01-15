# chatbot/models.py
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField()
    regno = models.CharField(max_length=20, unique=True, default='UNKNOWN')  # Provide a default value# Registration number

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    course_code = models.CharField(max_length=10, unique=True)
    course_name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    semester = models.CharField(max_length=20)
    schedule = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"

class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.FloatField()
    exam_date = models.DateField()

    def __str__(self):
        return f"Result: {self.student} in {self.course} - {self.score}"

class AssignmentDeadline(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignment_name = models.CharField(max_length=100)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.assignment_name} for {self.course} due on {self.due_date}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"
