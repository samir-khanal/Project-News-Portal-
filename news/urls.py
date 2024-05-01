from django.urls import path
from news.views import blog_delete, blog_update, index, blog, blog_add, blog_details, about, contact, news_details, category

urlpatterns = [
    path('', index, name='index'),
    path('blog', blog, name='blog'),
    path('blog/add', blog_add, name='blog_add'),
    path('blog/<slug>', blog_details, name='blog_details'),
    path('blog/<slug>/update', blog_update, name='blog_update'),
    path('blog/<slug>/delete',blog_delete, name='blog_delete'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('news/<slug>', news_details, name='news_details'),
    path('category/<slug>', category, name='category'),
]
