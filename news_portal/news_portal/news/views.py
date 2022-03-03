from datetime import datetime
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import *
from django.core.paginator import Paginator
from .forms import *


class PostList(ListView):
    model = Post
    paginate_by = 3
    template_name = 'news/posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        # context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post_select.html'
    context_object_name = 'posts'


def search(request):
    filtered = PostFilter(request.GET, queryset=Post.objects.all())
    paginator = Paginator(filtered.qs, 3)
    page_number = request.GET.get('page')
    page_obj1 = paginator.get_page(page_number)
    return render(request, 'news/search.html', {'page_obj1': page_obj1, 'filter': filtered})


# def add_post(request):
#     form = AddPost()
#     return render (request, 'news/add_post.html', {'form': form})

class CreatePost(CreateView):
    form_class = AddPost
    template_name = 'news/add_post.html'


class UpdatePost(UpdateView):
    model = Post
    form_class = AddPost
    template_name = 'news/update_post.html'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('pk')
        return Post.objects.get(pk=post_id)


class DeletePost(DeleteView):
    template_name = 'news/del_post.html'
    queryset = Post.objects.all()
    success_url = '/news_portal'
