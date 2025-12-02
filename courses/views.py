from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, StudentCourse
from .serializers import CourseSerializer, StudentCourseSerializer

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

@api_view(['POST'])
def add_studentcourse(request):
    serializer = StudentCourseSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            return Response(serializer.data, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
    return Response(serializer.errors, status=400)

# ==============================
# دالة البحث عن الكورسات
# ==============================
@api_view(['GET'])
def course_search(request):
    query = request.GET.get('q', '')  # مثال: ?q=Python
    courses = Course.objects.filter(name__icontains=query)  # تعديل من title -> name
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)




# -------------------- Get all student-course enrollments --------------------
@api_view(['GET'])
def list_student_courses(request):
    enrollments = StudentCourse.objects.all()
    serializer = StudentCourseSerializer(enrollments, many=True)
    return Response(serializer.data)

