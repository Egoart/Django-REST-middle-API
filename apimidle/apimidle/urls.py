"""apimidle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("user-generate/", views.UserGenerator.as_view()),
    path("todo-generate/", views.TodoGenerator.as_view()),
    path("photo-generate/", views.PhotoGenerator.as_view()),
    path("album-generate/", views.AlbumGenerator.as_view()),
    path("post-generate/", views.PostGenerator.as_view()),
    path("users/", views.UserList.as_view()),
    path("todos/", views.TodoList.as_view()),
    path("photos/", views.PhotoList.as_view()),
    path("albums/", views.AlbumList.as_view()),
    path("posts/", views.PostListView.as_view()),
    path("comments/", views.CommentFilterView.as_view()),
    path("posts/<int:pk>", views.SinglePost.as_view()),
    path("posts/<int:pk>/comments", views.SinglePostComments.as_view()),
    path("post-create/", views.CreatePost.as_view()),
]
