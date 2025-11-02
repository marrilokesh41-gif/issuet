from django.contrib import admin
from .models import Candidate

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "position", "location", "experience")
    search_fields = ("full_name", "email", "position", "tech_stack")
