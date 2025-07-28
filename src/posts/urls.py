from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView

from posts.views import BlogHome, BlogPostCreateView, BlogPostUpdateView, BlogPostDetailView, BlogPostDeleteView, SignUpView, AuthorProfileView

app_name = "posts"

urlpatterns = [
    path('home', (BlogHome.as_view()), name='home'),
    path('create/', login_required(BlogPostCreateView.as_view()), name='create'),
    path('edit/<str:slug>/',login_required(BlogPostUpdateView.as_view()) , name='edit'),
    path('delete/<str:slug>/',login_required(BlogPostDeleteView.as_view()) , name="delete"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('author/<str:username>/', AuthorProfileView.as_view(), name='author-profile'),
    path('<str:slug>/', BlogPostDetailView.as_view(), name='post'),

]
