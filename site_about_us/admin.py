from django.contrib import admin
from .models import AboutUs

from django.contrib import admin
from .models import AboutUs, AboutWork


# Register your models here.

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ["__str__", "email", "phone", "date_of_birth", "place_of_birth"]

    class meta:
        model = AboutUs


class AboutWorkAdmin(admin.ModelAdmin):
    list_display = ["__str__", "title", "description", "active"]
    list_editable = ["active"]

    class meta:
        model = AboutWork


admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(AboutWork, AboutWorkAdmin)