from django.contrib import admin
from .models import Works


class WorksAdmin(admin.ModelAdmin):
    list_display = ["__str__", "image", "active"]
    list_filter = ["active"]
    list_editable = ["active"]

    class meta:
        model = Works


admin.site.register(Works, WorksAdmin)
