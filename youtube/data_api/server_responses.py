# -*- coding: utf-8 -*-
from resources.main import Activity, Channel
from utils import youtube_get, error_factory, create_or_none, extra_kwargs_warning
from youtube.data_api.resources.supporting import PageInfo

ACTIVITIES_URL = "https://www.googleapis.com/youtube/v3/activities/"

CHANNELS_URL = "https://www.googleapis.com/youtube/v3/channels"


class Resource(object):
    accepted = []
    url = None

    @classmethod
    def get(cls, part, **kwargs):
        return youtube_get(cls.url, part=part, **kwargs)

    @classmethod
    def pop_extras(cls, kwargs):
        accepted = cls.accepted
        extras = dict()
        for key in kwargs:
            if key not in accepted:
                extras[key] = kwargs.pop(key)
        return extras

    @classmethod
    def list(cls, part, **kwargs):
        extras = cls.pop_extras(kwargs)
        extra_kwargs_warning(extras)

        response = cls.get(part, **kwargs)

        if 'error' in response:
            error_factory(response)
        return cls(**response)


class Activities(Resource):
    accepted = [
        'channelId', 'home', 'maxResults',
        'mine', 'pageToken', 'publishedAfter',
        'publishedBefore', 'regionCode', 'fields',
    ]

    url = ACTIVITIES_URL

    def __init__(self, kind=None, etag=None, pageInfo=None, nextPageToken=None, prevPageToken=None, items=None):
        self.kind = kind
        self.etag = etag
        self._pageInfo = pageInfo
        self.nextPageToken = nextPageToken
        self.prevPageToken = prevPageToken
        self._items = items or []
        self.parse()

    def parse(self):
        items = self._items
        self.items = [Activity(**item) for item in items]

        self.pageInfo = create_or_none(PageInfo, self._pageInfo)


class Channels(Resource):
    url = CHANNELS_URL
    accepted = [
        'categoryId', 'forUsername', 'id',
        'managedByMe', 'mine', 'mySubscribers',
        'maxResults', 'onBehalfOfContentOwner',
        'pageToken', 'fields',
    ]

    def __init__(self, kind=None, etag=None, pageInfo=None, nextPageToken=None, prevPageToken=None, items=None):
        self.kind = kind
        self.etag = etag
        self._pageInfo = pageInfo
        self.nextPageToken = nextPageToken
        self.prevPageToken = prevPageToken
        self._items = items or []
        self.parse()

    def parse(self):
        items = self._items
        self.items = [Channel(**item) for item in items]
        self.pageInfo = create_or_none(PageInfo, self._pageInfo)


__author__ = 'lalo'
