from django.shortcuts import render

from rest_framework import viewsets
from .models import Course, Discipline
from .serializers import CourseSerializer, DisciplineSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer