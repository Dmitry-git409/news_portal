from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import *


class PostListTest(ListView):
    model = Post
    template_name = 'news/posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post_select.html'
    context_object_name = 'posts'
