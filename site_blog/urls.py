from django.urls import path
from .views import BlogsList, blog_detail, BlogsListCategory, like, unlike

app_name = "blogs"

urlpatterns = [
    path('blogs/', BlogsList.as_view(), name="blog_list"),
    path('blogs/<category_name>/', BlogsListCategory.as_view(), name="blog_list_category"),
    path('blogs/<blogId>/<name>/', blog_detail, name="blog_list"),
    path('like/<blogId>/', like, name="like_blog"),
    path('unlike/<blogId>/', unlike, name="unlike_blog")
]
