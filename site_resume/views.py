from django.shortcuts import render
from .models import ResumeEducation, ResumeExperience, ResumeSkill


def resume(request):
    education = ResumeEducation.objects.get_active_resume_education()
    experience = ResumeExperience.objects.get_active_resume_experience()
    skill = ResumeSkill.objects.get_active_resume_skill()
    context = {
        "education": education,
        "experience": experience,
        "skill": skill,
    }
    return render(request, "resume/resume.html", context)
