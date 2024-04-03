from django.contrib import admin
from apps.exec import export_to_xlsx
from apps.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'email', 'phone', 'address', 'group']
    actions = [export_to_xlsx]


admin.site.register(Contact, ContactAdmin)
