
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

# Simple home page
def home(request):
    return HttpResponse("""
        <h2>Welcome to the Hiring Portal 🚀</h2>
        <p>This is your Django backend running successfully on Render.</p>
        <p><b>API Endpoint:</b> <a href='/api/candidates/'>/api/candidates/</a></p>
    """)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/candidates/', include('candidates.urls')),
]

# ✅ Serve media files (like resumes) in Render and development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
