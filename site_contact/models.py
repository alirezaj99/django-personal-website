from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(max_length=100, verbose_name="email")
    message = models.TextField(verbose_name="متن پیام")
    time = models.DateTimeField(auto_now_add=True, verbose_name="زمان ارسال پیام")
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده / نشده")

    class Meta:
        verbose_name = "تماس کاربر"
        verbose_name_plural = "تماس های کاربران"

    def __str__(self):
        return self.full_name
