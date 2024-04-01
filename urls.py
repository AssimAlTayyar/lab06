from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name='home'),  # Add this line for the root URL
    path('admin/', admin.site.urls),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/add/', views.StudentCreateView.as_view(), name='student_create'),
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/add/', views.CourseCreateView.as_view(), name='course_create'),
    path('details/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('', RedirectView.as_view(url='/students/'), name='home'),
]