
from django.urls import path
from .views import PostListCreateView, SerializerNotSetView

urlpatterns = [
    path('blog/posts', PostListCreateView.as_view(), name="post_list_create"),
    path('notset/', SerializerNotSetView.as_view(), name="notset_path"),
]
