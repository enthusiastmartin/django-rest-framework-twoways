
from django.conf.urls import include, url
from django.urls import path
from .views import PostListCreateView

urlpatterns = [
    path('blog/posts', PostListCreateView.as_view(), name="post_list_create"),

]
