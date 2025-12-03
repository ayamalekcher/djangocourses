from rest_framework import serializers
from .models import StudentCourse, Course, Student

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentCourseSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    # قبول IDs عند الإضافة فقط
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='student', write_only=True
    )
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), source='course', write_only=True
    )

    class Meta:
        model = StudentCourse
        fields = ['id', 'student', 'course', 'student_id', 'course_id']
