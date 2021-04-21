from django.db import models
import os
import random
from django.utils import timezone
from site_work_category.models import WorksCategory


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    random_num = random.randint(1, 989999999)
    name, ext = get_filename_ext(filename)
    final_name = f"{random_num}-{instance.title}{ext}"
    return f"works/{final_name}"


class WorksManager(models.Manager):
    def get_active_work(self):
        return self.get_queryset().filter(active=True)


class Works(models.Model):
    title = models.CharField(max_length=100, default="تصویر", verbose_name="تصویر")
    description = models.CharField(max_length=250, default="توضیحات", verbose_name="توضیحات")
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name="تصویر کار")
    categories = models.ManyToManyField(WorksCategory, blank=True, related_name="category",
                                        verbose_name="دسته بندی ها")

    time = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    active = models.BooleanField(default=False, verbose_name="فعال / غیرفعال")

    objects = WorksManager()

    class Meta:
        verbose_name = "کار"
        verbose_name_plural = "کارها"

    def __str__(self):
        return f"{self.title}-{self.id}"

    def get_image_or_default(self):
        try:
            return self.image.url
        except:
            return '/static/default/background-image.jpg'
