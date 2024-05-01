from re import T
from tabnanny import verbose
from tkinter import CASCADE
from turtle import title
from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.


class Setting(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to="images/", null=True, blank=True)
    favicon = models.ImageField(upload_to="images/", null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    google = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Settings'

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class News(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    intro = RichTextField(null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class Blog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    intro = RichTextField(null=True, blank=True)
    content = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.title
