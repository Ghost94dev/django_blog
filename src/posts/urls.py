from django.urls import path
from django.contrib.auth.decorators import login_required

from posts.views import BlogHome, BlogPostCreateView, BlogPostUpdateView, BlogPostDetailView, BlogPostDeleteView

app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('create/', login_required(BlogPostCreateView.as_view()), name='create'),
    path('<str:slug>/', BlogPostDetailView.as_view(), name='post'),
    path('edit/<str:slug>/',login_required(BlogPostUpdateView.as_view()) , name='edit'),
    path('delete/<str:slug>/',login_required(BlogPostDeleteView.as_view()) , name="delete"),


]
