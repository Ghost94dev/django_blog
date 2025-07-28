from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect


from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from posts.models import BlogPost



class AuthorProfileView(ListView):
    model = BlogPost
    template_name = 'posts/profile.html'
    context_object_name = 'posts'
    paginate_by = 5  # optional pagination

    def get_queryset(self):
        self.author = get_object_or_404(User, username=self.kwargs['username'])
        return BlogPost.objects.filter(author=self.author).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        return context






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
    fields = ['title', 'content', 'published','thumbnail']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"
    template_name = "posts/blogpost_list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('posts:home')  # or wherever you want