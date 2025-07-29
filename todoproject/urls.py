# todoproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from todo import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_views.task_list, name='task_list'),
    path('tasks/', include('todo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]