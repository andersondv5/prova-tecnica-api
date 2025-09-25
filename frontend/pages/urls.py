from django.urls import path
from . import views

urlpatterns = [
    path("courses/", views.courses_list, name="courses_list"),
    path("disciplines/", views.disciplines_list, name="disciplines_list"),
]

