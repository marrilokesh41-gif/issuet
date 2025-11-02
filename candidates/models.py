
from django.db import models

class Candidate(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    experience = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    tech_stack = models.TextField()
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)

    def __str__(self):
        return self.full_name
