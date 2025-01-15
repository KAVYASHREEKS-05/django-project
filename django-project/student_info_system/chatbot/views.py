from django.shortcuts import render,get_object_or_404
from .models import Student, Course, ExamResult, AssignmentDeadline, Enrollment
from django.http import HttpResponseRedirect 
from django.shortcuts import render, redirect
from .form import StudentForm,CourseForm,ExamForm,AssignmentForm,EnrollmentForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def chatbot_interface(request):
    return render(request, 'chatbot/chatbot.html')

def chatbot_response(request):
    question = request.GET.get('question', '').lower()  # Get the question and convert it to lowercase
    regno = request.GET.get('regno', '').strip()  # Get the registration number from the request
    response = "I'm sorry, I didn't understand that."
    chat_history = request.session.get('chat_history', [])  # Retrieve chat history from session

    if regno:
        try:
            student = Student.objects.get(regno=regno)
        except Student.DoesNotExist:
            response = "Student not found. Please provide a valid registration number."
            chat_history.append({"type": "response", "message": response})
            request.session['chat_history'] = chat_history
            return render(request, 'chatbot/chatbot.html', {'response': response, 'chat_history': chat_history})

        if "student" in question:
            if "name" in question:
                response = f"Student Name: {student.first_name} {student.last_name}"
            elif "email" in question:
                response = f"Email: {student.email}"
            elif "enrollment date" in question:
                response = f"Enrollment Date: {student.enrollment_date}"
            else:
                response = "Which student details would you like? Name, Email, or Enrollment Date?"

        elif "course" in question:
            enrollments = Enrollment.objects.filter(student=student)
            courses = [enrollment.course.course_name for enrollment in enrollments]
            response = f"{student.first_name} is enrolled in: " + ", ".join(courses) if courses else f"{student.first_name} is not enrolled in any courses."

        elif "exam result" in question:
            results = ExamResult.objects.filter(student=student)
            response = f"Exam results for {student.first_name}: " + ", ".join([f"{result.course.course_name} - {result.score}" for result in results]) if results else "No exam results found."

        elif "assignment" in question:
            enrollments = Enrollment.objects.filter(student=student)
            courses = [enrollment.course for enrollment in enrollments]
            assignments = AssignmentDeadline.objects.filter(course__in=courses)
            response = f"Assignments for {student.first_name}: " + ", ".join([f"{assignment.assignment_name} due on {assignment.due_date}" for assignment in assignments]) if assignments else "No assignments found."

        elif "enrollment" in question:
            enrollments = Enrollment.objects.filter(student=student)
            response = f"{student.first_name} is enrolled in: " + ", ".join([enrollment.course.course_name for enrollment in enrollments]) if enrollments else f"{student.first_name} is not enrolled in any courses."

    else:
        response = "Which student? Please provide the student's registration number (regno)."

    # Append the new question and response to the chat history
    chat_history.append({"type": "question", "message": question})
    chat_history.append({"type": "response", "message": response})

    # Save chat history back to the session
    request.session['chat_history'] = chat_history

    return render(request, 'chatbot/chatbot.html', {'response': response, 'chat_history': chat_history})

def clear_chat(request):
    # Clear the chat history stored in the session
    if 'chat_history' in request.session:
        del request.session['chat_history']
        
    
    # Redirect to the chatbot page to start fresh
    return redirect('chatbot_interface')





def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('add_course')  # Redirect to a success page after saving
    else:
        form = StudentForm()
    return render(request, 'chatbot/add_student.html', {'form': form})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('result')  # Redirect to a success page after saving
    else:
        form = CourseForm()
    return render(request, 'chatbot/add_course.html', {'form': form})
def add_result(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('assignment')  # Redirect to a success page after saving
    else:
        form = ExamForm()
    return render(request, 'chatbot/result.html', {'form': form})
def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page after saving
    else:
        form =AssignmentForm()
    return render(request, 'chatbot/assignment.html', {'form': form})
def enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page after saving
    else:
        form =EnrollmentForm()
    return render(request, 'chatbot/enrollment.html', {'form': form})

def student_details(request):
    return render(request,'chatbot/student_details.html')




def success(request):
    return render(request,'chatbot/success.html')
def dashboard(request):
    return render(request, 'chatbot/dashboard.html')

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
    else:
        form = AuthenticationForm()
    return render(request, 'chatbot/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')  


