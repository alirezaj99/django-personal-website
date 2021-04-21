from django.urls import path
from .views import contact, success_contact

app_name = "contact"

urlpatterns = [
    path('contact/', contact, name="contact"),
    path('success-send-message/', success_contact, name="success_contact"),
]
