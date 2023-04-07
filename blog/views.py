from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy

from .models import Post
from .forms import NewPostForm


# def posts_list_view(request):
#     # posts_list = Post.objects.all()
#     posts_list = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/posts_list.html', {'posts_list': posts_list})

class PostListView(generic.ListView):
    # model = Post  # --> Post.objects.all()
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')


# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     post = None
#     #     print('excepted')
#     return render(request, 'blog/post_detail.html', {'post': post})


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'  # default get from model name --> Post = post


# def post_create_view(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # form = NewPostForm()
#             return redirect('posts_list')  # return redirect(reverse('posts_list'))
#
#     else:
#         form = NewPostForm()
#
#     return render(request, 'blog/post_create.html', {'form': form})
#
#     # if request.method == 'POST':
#     #     post_title = request.POST.get('title')
#     #     post_text = request.POST.get('text')
#     #     user = User.objects.all()[0]
#     #     Post.objects.create(
#     #         title=post_title,
#     #         text=post_text,
#     #         author=user,
#     #         status='pub'
#     #     )
#     # else:
#     #     print('get request')
#     # return render(request, 'blog/post_create.html')


class PostCreateView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/post_create.html'


# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#
#     if form.is_valid():
#         form.save()
#         return redirect('posts_list')
#
#     return render(request, 'blog/post_create.html', {'form': form})


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    # fields = ['title', 'text']
    template_name = 'blog/post_create.html'


# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
#
#     return render(request, 'blog/post_delete.html', {'post': post})


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')

    # def get_success_url(self):
    #     return reverse('posts_list')
