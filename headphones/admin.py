from django.contrib import admin
from . models import Headphones


class HeadphonesAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity")

admin.site.register(Headphones, HeadphonesAdmin)
