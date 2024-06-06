from django.contrib import admin
from .models import Blog, Tag, Contact, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ('likes',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Contact)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'blog')
