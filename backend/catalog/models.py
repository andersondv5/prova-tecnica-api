from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Discipline(models.Model):
    course = models.ForeignKey(Course, related_name="disciplines", on_delete=models.CASCADE)
    workload = models.PositiveIntegerField(help_text="Carga horária em horas")

    class Meta:
        unique_together = ('course', 'name')

    def __str__(self):
        return f"{self.name} ({self.course.name})"