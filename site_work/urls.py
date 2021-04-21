from django.urls import path
from .views import WorkList

app_name = "works"

urlpatterns = [
    path("works/", WorkList.as_view(), name="work_list")
]
