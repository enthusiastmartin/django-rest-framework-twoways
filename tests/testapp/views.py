from rest_framework import generics

from rest_framework_twoways.mixins import  TwoWaySerializerMixin
from tests.testapp.models import Post
from tests.testapp.serializers import PostInputSerializer, PostOutputSerializer


class PostListCreateView(TwoWaySerializerMixin, generics.ListCreateAPIView):
    input_serializer_class = PostInputSerializer
    output_serializer_class = PostOutputSerializer

    queryset = Post.objects.all()


class SerializerNotSetView(TwoWaySerializerMixin, generics.ListCreateAPIView):
    queryset = Post.objects.all()
