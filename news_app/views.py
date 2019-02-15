from .models import Post
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
# autorization and authentification
from django.contrib.auth.mixins import LoginRequiredMixin
# pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# CBVs
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# for visitors:


def post_detail(request, year, month, day, slug_url):
    post = get_object_or_404(Post, slug=slug_url,
                             status='published',
                             publishtime__year=year,
                             publishtime__month=month,
                             publishtime__day=day)
    return render(request,
                  'news_app/post_detail.html',
                  {'post': post})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 12
    template_name = 'news_app/post_list.html'


class UserPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'news_app/post_list.html'
    paginate_by = 12

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Post.published.filter(author__pk=pk).order_by('-publishtime')


# for aurhors:
class CurrentUserPostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'current_user_posts'
    template_name = 'news_app/current_user_post_list.html'
    paginate_by = 20

    def get_queryset(self):
        return Post.objects.filter(author__id=self.request.user.id).order_by('-createtime')


class CurrentUserPostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'news_app/current_user_post_detail.html'
    def get_queryset(self):
        return Post.objects.filter(author__id=self.request.user.id)


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'news_app/post_create.html'
    model = Post
    fields = ['title', 'description', 'image', 'body', 'status', 'updated']
    success_url = reverse_lazy('news_app:current_user_post_list')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object = form.save()
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    template_name = 'news_app/post_update.html'
    model = Post
    fields = ['title', 'description', 'image', 'body', 'status', 'updated']
    success_url = reverse_lazy('news_app:current_user_post_list')

    def get_queryset(self):
        return Post.objects.filter(author__id=self.request.user.id)

class DeletePostView(LoginRequiredMixin, DeleteView):
    template_name = 'news_app/post_delete.html'
    model = Post
    success_url = reverse_lazy('news_app:current_user_post_list')

    def get_queryset(self):
        return Post.objects.filter(author__id=self.request.user.id)
