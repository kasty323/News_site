from django.urls import path
from django.contrib import admin
from news.views import article_list, article_detail, article_create, article_update, article_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', article_list, name='article_list'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
    path('article/create/', article_create, name='article_create'),
    path('article/update/<int:pk>/', article_update, name='article_update'),
    path('article/delete/<int:pk>/', article_delete, name='article_delete'),
]
