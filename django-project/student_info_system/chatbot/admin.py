# chatbot/admin.py
from django.contrib import admin
from .models import Student, Course, ExamResult, AssignmentDeadline, Enrollment

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(ExamResult)
admin.site.register(AssignmentDeadline)
admin.site.register(Enrollment)
