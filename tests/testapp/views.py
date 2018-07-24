from rest_framework import generics

from rest_framework_twoways.views import TwoWayAPiView
from tests.testapp.models import Post
from tests.testapp.serializers import PostInputSerializer, PostOutputSerializer


class PostListCreateView(TwoWayAPiView, generics.ListCreateAPIView):
    input_serializer_class = PostInputSerializer
    output_serializer_class = PostOutputSerializer

    queryset = Post.objects.all()


class SerializerNotSetView(TwoWayAPiView, generics.ListCreateAPIView):
    queryset = Post.objects.all()
