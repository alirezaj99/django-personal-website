from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ["__str__", "email", "time", "is_read"]
    list_filter = ["is_read"]
    list_editable = ["is_read"]
    search_fields = ["full_name", "message"]

    class meta:
        model = Contact


admin.site.register(Contact, ContactAdmin)
