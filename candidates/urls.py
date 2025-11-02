
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CandidateListCreateView.as_view(), name='candidate-list-create'),
]
