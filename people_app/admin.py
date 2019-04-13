from django.contrib import admin
from .models import Profile, Structure
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name",)}


# +"second_name"+"patronymic",
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Structure)
