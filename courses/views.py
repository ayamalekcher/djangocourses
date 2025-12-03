from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, StudentCourse
from .serializers import CourseSerializer, StudentCourseSerializer

# ---------------- COURSES ----------------
@api_view(['GET'])
def list_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# ---------------- STUDENTCOURSE ----------------
@api_view(['POST'])
def add_studentcourse(request):
    serializer = StudentCourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def list_studentcourses(request):
    student_courses = StudentCourse.objects.all()
    data = []
    for sc in student_courses:
        data.append({
            "id": sc.id,
            "student": {
                "id": sc.student.id,
                "name": sc.student.name,
                "email": sc.student.email
            },
            "course": {
                "id": sc.course.id,
                "name": sc.course.name,
                "category": sc.course.category
            }
        })
    return Response(data)
