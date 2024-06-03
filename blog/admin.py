from django.contrib import admin
from .models import Blog, Tag


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'tag')
    list_filter = ('likes',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
# Register your models here.
