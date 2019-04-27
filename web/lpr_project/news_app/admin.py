from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'createtime', 'publishtime', 'status')
    list_filter = ('status', 'createtime', 'publishtime', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'createtime'
    ordering = ['-createtime']


admin.site.register(Post, PostAdmin)
