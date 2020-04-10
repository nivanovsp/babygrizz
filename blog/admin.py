from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user', 'created', 'publish')
    list_filter = ('title', 'category', 'user', 'created', 'publish')
    search_fields = ('title', 'category', 'user', 'created', 'publish')
    readonly_fields = ('created',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)



# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
