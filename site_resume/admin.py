from django.contrib import admin
from .models import ResumeEducation, ResumeExperience, ResumeSkill

admin.site.register(ResumeEducation)
admin.site.register(ResumeExperience)
admin.site.register(ResumeSkill)
