from django.db import models
import os
import random


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    random_num = random.randint(1, 989999999)
    name, ext = get_filename_ext(filename)
    final_name = f"{random_num}-{instance.first_name}-{instance.last_name}{ext}"
    return f"about_us/{final_name}"


def upload_image_path_about_work(instance, filename):
    random_num = random.randint(1, 989999999)
    name, ext = get_filename_ext(filename)
    final_name = f"{random_num}-{instance.title}{ext}"
    return f"about_us/about_work/{final_name}"


class AboutUs(models.Model):
    first_name = models.CharField(max_length=250, verbose_name="نام", default="نام")
    last_name = models.CharField(max_length=250, verbose_name="نام خانوادگی", default="نام خانوادگی")
    short_description = models.CharField(max_length=100, verbose_name="توضیح کوتاه", default="توضیح کوتاه")
    email = models.EmailField(max_length=100, verbose_name="ایمیل", default="ایمیل")
    phone = models.CharField(max_length=150, verbose_name="شماره تماس", default="شماره تماس")
    date_of_birth = models.CharField(max_length=60, verbose_name="تاریخ تولد", default="تاریخ تولد")
    place_of_birth = models.CharField(max_length=100, verbose_name="مکان تولد", default="مکان تولد")
    about_text = models.TextField(verbose_name="توضیحات درباره من", default="توضیحات درباره من")
    facebook = models.CharField(max_length=40, verbose_name="آیدی لینکدین", default="facebook")
    twitter = models.CharField(max_length=40, verbose_name="آیدی توییتر", default="twitter")
    instagram = models.CharField(max_length=40, verbose_name="آیدی اینستاگرام", default="instagram")
    profile_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name="عکس پروفایل")

    class Meta:
        verbose_name = "درباره من"
        verbose_name_plural = "درباره من"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_image_or_default(self):
        try:
            return self.profile_image.url
        except:
            return '/static/default/profile.jpg'


class AboutWorkManager(models.Manager):
    def get_active_about_work(self):
        return self.get_queryset().filter(active=True)


class AboutWork(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.CharField(max_length=400, verbose_name="توضیحات")
    about_work_image = models.ImageField(upload_to=upload_image_path_about_work, null=True, blank=True,
                                         verbose_name="آیکون")
    active = models.BooleanField(default=False, verbose_name="فعال / غیرفعال")
    objects = AboutWorkManager()

    class Meta:
        verbose_name = "درباره من کاری که انجام می دهم"
        verbose_name_plural = "درباره من کارهایی که انجام می دهم"

    def __str__(self):
        return self.title

    def get_image_or_default(self):
        try:
            return self.about_work_image.url
        except:
            return '/static/default/icon.png'
