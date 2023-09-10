from django.db import models

class Professor(models.Model):
    name = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    faculty = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.name
