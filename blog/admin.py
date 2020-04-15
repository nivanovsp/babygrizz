from django.contrib import admin
from .models import Blog, Comment, Contact


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


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'sent_on', 'processed')
    list_filter = ('name', 'email', 'message', 'sent_on', 'processed')
    search_fields = ('name', 'email', 'message', 'sent_on')
    actions = ['contact_processed']

    def contact_processed(self, request, queryset):
        queryset.update(processed=True)


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)
