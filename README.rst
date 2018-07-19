django-rest-framework-twoways
============

Extension to Django REST Framework to make it eaiser to set different serializer for input and output of one view.

Note : still in development - although ready to use.

Documentation
------------

To do ...

Installation
------------

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/enthusiastmartin/django-emailauth.git#egg=djangoemailauth

Usage
-----

Very simple usage. You can use provided mixin or view.

.. code-block:: python

    from rest_frame_work_twoways.views import TwoWayAPiView

    class YourView(TwoWayAPIView):
        input_serializer_class = PostSerializer
        output_serializer_class = GetSerializer


Only mixin:

.. code-block:: python

    from rest_frame_work_twoways.mixins import TwoWaySerializerMixin

    class YourView(TwoSerializerMixin, generics.ListCreateAPIView):
        input_serializer_class = PostSerializer
        output_serializer_class = GetSerializer


