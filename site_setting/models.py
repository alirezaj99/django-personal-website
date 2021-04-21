from django.db import models
import os
import random
from django.db.models.signals import pre_delete
from django.dispatch import receiver


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    random_num = random.randint(1, 989999999)
    name, ext = get_filename_ext(filename)
    final_name = f"{random_num}-{instance.title}{ext}"
    return f"site-setting/background-image/{final_name}"


def upload_image_path_icon(instance, filename):
    random_num = random.randint(1, 989999999)
    name, ext = get_filename_ext(filename)
    final_name = f"{random_num}-{instance.title}{ext}"
    return f"site-setting/icon/{final_name}"


class BackgroundImage(models.Model):
    title = models.CharField(max_length=120, default="تصویر پس زمینه", verbose_name="تصویر پس زمینه")
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name="عکس پروفایل")

    class Meta:
        verbose_name = "تصویر پس زمینه"
        verbose_name_plural = "تصاویر پس زمینه"

    def __str__(self):
        return f"{self.title} {self.id}"

    def get_image_or_default(self):
        try:
            return self.image.url
        except:
            return '/static/default/background-image.jpg'


class MainSetting(models.Model):
    title = models.CharField(max_length=120, default="عنوان سایت", verbose_name="عنوان سایت")
    icon = models.ImageField(upload_to=upload_image_path_icon, null=True, blank=True, verbose_name="عکس پروفایل")
    footer = models.CharField(max_length=250, default="فوتر سایت", verbose_name="فوتر سایت")

    class Meta:
        verbose_name = "آیکون سایت و فوتر"
        verbose_name_plural = "آیکون های سایت و فوتر"

    def __str__(self):
        return f"{self.title} {self.id}"

    def get_image_or_default(self):
        try:
            return self.icon.url
        except:
            return '/static/default/background-image.jpg'
