from django.shortcuts import render, redirect

from site_about_us.models import AboutUs
from site_setting.models import BackgroundImage, MainSetting


def view_404(request, exception):
    context = {

    }
    return render(request, "shared/404.html", context)


def view_403(request, exception):
    context = {

    }
    return render(request, "shared/403.html", context)


def view_400(request, exception):
    context = {

    }
    return render(request, "shared/400.html", context)


def view_500(request):
    context = {

    }
    return render(request, "shared/500.html", context)


def home_page(request):
    return redirect("about_us:about_me")


def footer(request):
    setting = MainSetting.objects.first()

    context = {
        "setting": setting
    }
    return render(request, "shared/Footer.html", context)


def header(request):
    about_us = AboutUs.objects.first()

    context = {
        "about_us": about_us
    }
    return render(request, "shared/Header.html", context)


def header_image_background(request):
    background_image = BackgroundImage.objects.first()
    context = {
        "background_image": background_image
    }
    return render(request, "shared/header_image_background.html", context)


def header_references(request):
    setting = MainSetting.objects.first()
    context = {
        "setting": setting
    }
    return render(request, "shared/_HeaderReferences.html", context)
