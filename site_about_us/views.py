from django.shortcuts import render
from .models import AboutUs, AboutWork


def about_me(request):
    about_us = AboutUs.objects.first()
    about_work = AboutWork.objects.get_active_about_work()
    context = {
        "about_us": about_us,
        "about_work": about_work
    }
    return render(request, "about/about_us.html", context)
