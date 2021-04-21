from django.db import models


class WorksCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    name = models.CharField(max_length=150, verbose_name="عنوان انگلیسی")

    def __str__(self):
        return f"{self.title} - {self.name}"

    class Meta:
        verbose_name = "دسته بندی کار"
        verbose_name_plural = "دسته بندی های کار"
