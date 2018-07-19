from django import forms
from rest_framework.generics import GenericAPIView

from .mixins import TwoWaySerializerMixin


class TwoWayAPiView(TwoWaySerializerMixin, GenericAPIView):
    pass
