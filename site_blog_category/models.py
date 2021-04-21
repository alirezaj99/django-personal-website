from django.db import models


class BlogsCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    name = models.CharField(max_length=150, verbose_name="عنوان در url")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی وبلاگ"
        verbose_name_plural = "دسته بندی های وبلاگ"

    def get_category_url(self):
        return f"/blogs/{self.name}"
