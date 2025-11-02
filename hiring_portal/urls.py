
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse("""
        <h1>Welcome to the Hiring Portal</h1>
        <p>This is your Django backend running successfully on Render 🚀</p>
        <p>Use the API endpoint: <a href="/api/candidates/">/api/candidates/</a></p>
    """)


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/candidates/', include('candidates.urls')),
]
