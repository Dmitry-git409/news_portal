from django.urls import path
from .views import *

urlpatterns = [
    path('', PostListTest.as_view(), name='home'),
    path('<int:pk>/', PostDetail.as_view(), name='post_list')
]
