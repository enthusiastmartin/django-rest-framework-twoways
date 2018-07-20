# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst') as f:
    README = f.read()


setup(
    name='djangorestframework-twoways',
    version='0.0.1',
    url='https://github.com/enthusiastmartin/django-rest-framework-twoways',
    license='MIT',
    long_description=README,
    description='Different serializers for GET and POST',
    author='enthusiast martin',
    author_email='enthusiastmartin@gmail.com',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'djangorestframework',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
