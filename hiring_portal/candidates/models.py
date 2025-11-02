
from django.db import models

class Candidate(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    experience = models.CharField(max_length=10, blank=True)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    tech_stack = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.full_name
