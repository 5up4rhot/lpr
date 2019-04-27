from django.contrib import admin

from .models import Principle, Opinion, Reform, QA
# Register your models here.
admin.site.register(Principle)
admin.site.register(Opinion)
admin.site.register(Reform)
admin.site.register(QA)
