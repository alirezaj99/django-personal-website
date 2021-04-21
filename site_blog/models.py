from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
import os
import random

from site_blog_category.models import BlogsCategory


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    random_num = random.randint(1, 989999999)
    name, ext = get_filename_ext(filename)
    final_name = f"{random_num}-{instance.title}{ext}"
    return f"blogs/{final_name}"


class BlogsManager(models.Manager):
    def get_active_blogs(self):
        return self.get_queryset().filter(active=True)

    def get_by_id(self, blog_id):
        qs = self.get_queryset().filter(id=blog_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get_blogs_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)


class Blogs(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان", default="عنوان")
    description = models.CharField(max_length=400, verbose_name="توضیحات کوتاه", default="توضیحات کوتاه")
    body = RichTextField(blank=True, null=True, verbose_name="بدنه اصلی")
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
                              verbose_name="تصویر اصلی")
    categories = models.ManyToManyField(BlogsCategory, blank=True, verbose_name="دسته بندی وبلاگ")
    like = models.ManyToManyField(User, related_name="BlogsLikes", blank=True, verbose_name="لایک")
    time = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    active = models.BooleanField(default=False, verbose_name="فعال / غیرفعال")

    objects = BlogsManager()

    class Meta:
        verbose_name = "بلاگ"
        verbose_name_plural = "بلاگ ها"

    def __str__(self):
        return self.title

    def get_image_or_default(self):
        try:
            return self.image.url
        except:
            return '/static/default/background-image.jpg'

    def get_absolute_url(self):
        return f"/blogs/{self.id}/{self.title.replace(' ', '-')}"


class CommentManager(models.Manager):
    def get_active_comment(self):
        return self.get_queryset().filter(active=True)


class Comment(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name="comments", verbose_name="بلاگ")
    name = models.CharField(max_length=100, verbose_name="نام")
    text = models.TextField(verbose_name="نظر")
    email = models.EmailField(max_length=100, verbose_name="ایمیل")
    date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ")
    active = models.BooleanField(default=False, verbose_name="فعال / غیرفعال")

    objects = CommentManager()

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    def __str__(self):
        return f"{self.blog} - {self.name}"
