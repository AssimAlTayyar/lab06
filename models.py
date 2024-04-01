from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'myschool'

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'myschool'