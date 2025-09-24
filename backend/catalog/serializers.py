from rest_framework import serializers
from .models import Course, Discipline

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = ['id', 'name', 'workload', 'course']

class CourseSerializer(serializers.ModelSerializer):
    disciplines = DisciplineSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'disciplines']
        