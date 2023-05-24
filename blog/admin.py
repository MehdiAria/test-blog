from django.contrib import admin

from .models import Post, Category, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'body', 'categories', 'author', 'slug']
    readonly_fields = ['title',]
    search_fields = ['author__username']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('posts', 'name', 'body',)
