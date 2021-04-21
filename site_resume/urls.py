from django.urls import path
from .views import resume

app_name = "resumes"

urlpatterns = [
    path('resume/', resume, name="resume")
]
