from django.urls import path
from .views import about_me

app_name = "about_us"

urlpatterns = [
    path('', about_me, name="about_me"),
]
