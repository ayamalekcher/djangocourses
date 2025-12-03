from django.db import models

class Student(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Course(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    schedule = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StudentCourse(models.Model):
    student_id = models.IntegerField()  # ID men Spring Boot
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")


    def __str__(self):
        return f"Student {self.student} enrolled in {self.course}"
