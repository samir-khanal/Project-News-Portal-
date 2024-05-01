from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Setting)
class AdminSetting(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'logo', 'favicon',
                    'facebook', 'twitter', 'instagram', 'linkedin', 'youtube', 'google']


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['category_name']


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ['title', 'date', 'author', 'image', 'category', 'views']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ['title', 'date', 'author', 'image']
    prepopulated_fields = {'slug': ['title']}
