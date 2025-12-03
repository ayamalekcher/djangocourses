from rest_framework import serializers
from .models import StudentCourse, Student, Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentCourseSerializer(serializers.ModelSerializer):
    # استخدام PrimaryKeyRelatedField للـ POST
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(),
        source='student'
    )
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='course'
    )

    class Meta:
        model = StudentCourse
        fields = ['id', 'student_id', 'course_id']
