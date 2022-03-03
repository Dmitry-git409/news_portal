from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<int:pk>/', PostDetail.as_view(), name='post_list'),
    path('search/', search, name='search'),
    path('add_post/', CreatePost.as_view(), name='add_post'),
    path('update_post/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('del_post/<int:pk>', DeletePost.as_view(), name='del_post'),
]
