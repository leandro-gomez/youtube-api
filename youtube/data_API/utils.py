# -*- coding: utf-8 -*-
import requests
from youtube.data_API.exceptions import YouTubeException
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


def create_error(response):
    return YouTubeException(response)


def parse(response, to_python=True):
    python_response = response.json()
    if to_python:
        return python_response
    json_response = json.dumps(python_response)
    return json_response


def youtube_get(url, **kwargs):
    to_python = kwargs.pop('to_python', True)

    params = get_default_params()
    params.update(kwargs)
    response = requests.get(url, params=params)

    response = parse(response, to_python)
    return response


__author__ = 'lalo'
