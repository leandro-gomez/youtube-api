#! coding: utf-8
import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='youtube-api-wrapper',
    version='0.1',
    packages=['youtube', 'youtube.data', 'youtube.data.resources'],
    include_package_data=True,
    license='BSD License',
    install_requires=['iso8601', 'requests'],
    description='Python Youtube Data API',
    long_description=README,
    url='https://github.com/lalo73/youtube-api/',
    author='Leandro Gomez',
    author_email='leandro.gz73@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
    ],
)

__author__ = 'lgomez'
