from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Course, StudentCourse
from .serializers import CourseSerializer, StudentSerializer, StudentCourseSerializer


# ==============================
# Courses
# ==============================
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

# ==============================
# Student-Course
# ==============================
@api_view(['POST'])
def add_studentcourse(request):
    try:
        student_id = request.data.get('student_id')
        course_id = request.data.get('course_id')
        if not student_id or not course_id:
            return Response({"error": "student_id and course_id are required"}, status=400)

        student = Student.objects.get(id=student_id)
        course = Course.objects.get(id=course_id)

        # Prevent duplicates
        obj, created = StudentCourse.objects.get_or_create(student=student, course=course)
        serializer = StudentCourseSerializer(obj)
        return Response(serializer.data, status=201 if created else 200)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=400)

# ==============================
# Search courses
# ==============================
@api_view(['GET'])
def course_search(request):
    query = request.GET.get('q', '')
    courses = Course.objects.filter(name__icontains=query)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

# ==============================
# List student-course enrollments
# ==============================
@api_view(['GET'])
def list_studentcourses(request):
    student_courses = StudentCourse.objects.all()
    data = []
    for sc in student_courses:
        data.append({
            "id": sc.id,
            "student": {
                "id": sc.student.id,
                "firstName": sc.student.name.split()[0] if sc.student.name else "",
                "lastName": " ".join(sc.student.name.split()[1:]) if len(sc.student.name.split()) > 1 else ""
            },
            "course": {
                "id": sc.course.id,
                "name": sc.course.name,
                "category": sc.course.category
            }
        })
    return Response(data)
