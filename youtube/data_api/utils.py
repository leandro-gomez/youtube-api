# -*- coding: utf-8 -*-
import warnings
import requests
from youtube.data_api.exceptions import YouTubeException
from youtube.settings import API_KEY
import json


def create_or_none(cls, value):
    if value:
        return cls(**value)
    else:
        return None


def get_default_params():
    params = {'key': API_KEY, 'headers': {'content-type': 'application/json'}}
    return params


def extra_kwargs_warning(kwargs):
    if kwargs:
        message = "This method has receive extra params: {extra}".format(extra=kwargs)
        warnings.warn(message, SyntaxWarning)


def error_factory(response):
    return YouTubeException(response)


def parse(response, to_python=True):
    python_response = response.json()
    if to_python:
        return python_response
    json_response = json.dumps(python_response)
    return json_response


def get_non_none_kwargs(kwargs):
    return dict((k, v) for k, v in kwargs.iteritems() if v is not None)


def get_params(kwargs):
    params = get_default_params()
    non_none_params = get_non_none_kwargs(kwargs)
    params.update(non_none_params)
    return params


def youtube_get(url, **kwargs):
    to_python = kwargs.pop('to_python', True)

    params = get_params(kwargs)

    response = requests.get(url, params=params)
    response = parse(response, to_python)
    return response


__author__ = 'lalo'
