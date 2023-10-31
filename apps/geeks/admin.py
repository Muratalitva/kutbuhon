from django.contrib import admin
from apps.geeks.models import Settings, Contact,Gallery

@admin.register(Settings)
class GeeksAdmin(admin.ModelAdmin):
    list_display = ['title', 'descriptions']

@admin.register(Contact)
class GeeksAdmin(admin.ModelAdmin):
    list_display = ['phone', 'instagram', 'whatsapp']


admin.site.register(Gallery)