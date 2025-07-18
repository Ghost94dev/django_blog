from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse


from posts.models import BlogPost


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "posts/blogpost_delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("posts:home")




class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "posts/blogpost_detail.html"
    context_object_name = "post"



class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = ['title', 'content', 'published']


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title', 'content',]


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"
    template_name = "posts/blogpost_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)
