# chatbot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chatbot_interface/', views.chatbot_interface, name='chatbot_interface'),
    path('response/', views.chatbot_response, name='chatbot_response'),
     path('chatbot_interface/', views.clear_chat, name='clear_chat'),
     path('add_student/', views.add_student, name='add_student'),
     path('add_course/', views.add_course, name='add_course'),
     path('result/', views.add_result, name='result'),
     path('assignment/', views.add_assignment, name='assignment'),
     path('enrollment/', views.enrollment, name='enrollment'),
    path('success/', views.success, name='success'),  
    path('dashboard/',views.dashboard,name="dashboard"),
     path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
