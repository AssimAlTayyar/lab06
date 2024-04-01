from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Student, Course
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
class StudentListView(ListView):
    model = Student
    template_name = 'myapp/student_list.html'
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'myapp/student_form.html'
    fields = ['name', 'age', 'email', 'courses']
    success_url = reverse_lazy('student_list')

class CourseListView(ListView):
    model = Course
    template_name = 'myapp/course_list.html'
    context_object_name = 'courses'

class CourseCreateView(CreateView):
    model = Course
    template_name = 'myapp/course_form.html'
    fields = ['name']
    success_url = reverse_lazy('course_list')

class StudentDetailView(DetailView):
    model = Student
    template_name = 'myapp/student_detail.html'
    context_object_name = 'student'