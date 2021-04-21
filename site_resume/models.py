from django.db import models


class ResumeEducationManager(models.Manager):
    def get_active_resume_education(self):
        return self.get_queryset().filter(active=True)


class ResumeEducation(models.Model):
    place = models.CharField(max_length=300, verbose_name="مکان تحصیل", default="مکان تحصیل")
    time = models.CharField(max_length=100, verbose_name="بازه زمان تحصیل", default="بازه زمان تحصیل")
    description = models.CharField(max_length=400, verbose_name="توضیحات تحصیل", default="توضیحات تحصیل")
    active = models.BooleanField(default=False, verbose_name="فعال / غیرفعال")

    objects = ResumeEducationManager()

    class Meta:
        verbose_name = "تحصیل من"
        verbose_name_plural = "تحصیلات من"

    def __str__(self):
        return f"{self.place}-{self.time}"


class ResumeExperienceManager(models.Manager):
    def get_active_resume_experience(self):
        return self.get_queryset().filter(active=True)


class ResumeExperience(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان تجربه", default="عنوان تجربه")
    time = models.CharField(max_length=100, verbose_name="بازه زمان تجربه", default="بازه زمان تجربه")
    description = models.CharField(max_length=400, verbose_name="توضیحات تجربه", default="توضیحات تجربه")
    active = models.BooleanField(default=False, verbose_name="فعال / غیرفعال")

    objects = ResumeExperienceManager()

    class Meta:
        verbose_name = "تجربه من"
        verbose_name_plural = "تجربه های من"

    def __str__(self):
        return f"{self.title}-{self.time}"


class ResumeSkillManager(models.Manager):
    def get_active_resume_skill(self):
        return self.get_queryset().filter(active=True)


class ResumeSkill(models.Model):
    title = models.CharField(max_length=100, default="عنوان مهارت من", verbose_name="عنوان مهارت من")
    percent = models.IntegerField(verbose_name="درصد مهارت", default=0)
    active = models.BooleanField(default=False, verbose_name="فعال / غیرفعال")

    objects = ResumeSkillManager()

    class Meta:
        verbose_name = "مهارت من"
        verbose_name_plural = "مهارت های من"

    def __str__(self):
        return f"{self.title}-{self.percent}"
