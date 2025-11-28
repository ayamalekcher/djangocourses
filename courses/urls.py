from django.urls import path, include   # ✅ include ajouté
from . import views

urlpatterns = [
    
   
    
    # 🔹 Endpoints de ton app courses
    path('', views.list_courses, name='list_courses'),            # GET /courses/
    path('add/', views.add_course, name='add_course'),           # POST /courses/add/
    path('search/', views.course_search, name='course_search'),  # GET /courses/search/?q=...
    path('studentcourses/add/', views.add_studentcourse, name='add_studentcourse'),  # POST /courses/studentcourses/add/
]
