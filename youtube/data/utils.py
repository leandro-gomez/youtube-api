# -*- coding: utf-8 -*-
import requests
from youtube.data.exceptions import YouTubeException
from youtube.settings import API_KEY


def create_or_none(cls, value):
    if value:
        return cls(**value)
    else:
        return None


def get_default_params():
    params = {}
    if API_KEY:
        params['key'] = API_KEY
    return params


def error_factory(response):
    return YouTubeException(response)


def get_params(**kwargs):
    params = get_default_params()
    params.update(kwargs)
    return params


def youtube_get(url, get_method=requests.get, **kwargs):
    params = get_params(**kwargs)
    response = get_method(url, params=params)
    return response


__author__ = 'lalo'
