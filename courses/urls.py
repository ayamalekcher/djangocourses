from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_courses),            # GET /courses/ → قائمة الكورسات
    path('add/', views.add_course),          # POST /courses/add/ → إضافة كورس
    path('search/', views.course_search),    # GET /courses/search/?q=... → البحث
    path('studentcourses/add/', views.add_studentcourse),  # POST /courses/studentcourses/add/
]
