from django import forms
from .models import Student,Course,ExamResult,AssignmentDeadline,Enrollment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__' 

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__' 
class ExamForm(forms.ModelForm):
    class Meta:
        model = ExamResult
        fields = '__all__' 
class AssignmentForm(forms.ModelForm):
    class Meta:
        model =AssignmentDeadline
        fields = '__all__' 
        
class EnrollmentForm(forms.ModelForm):
    class Meta:
        model =Enrollment
        fields = '__all__' 
        
