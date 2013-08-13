# -*- coding: utf-8 -*-
from resources.types import Activity, Channel, GuideCategory
from utils import youtube_get, error_factory, create_or_none, extra_kwargs_warning
from youtube.data.resources.nested_fields import PageInfo

ACTIVITIES_URL = "https://www.googleapis.com/youtube/v3/activities/"

CHANNELS_URL = "https://www.googleapis.com/youtube/v3/channels"

GUIDE_CATEGORIES_URL = "https://www.googleapis.com/youtube/v3/guideCategories"


class Resource(object):
    """
    Abstract class of Resource YouTube Data API
    """
    accepted = []
    url = None

    def __init__(self, **kwargs):
        self.extra = kwargs

    @classmethod
    def get(cls, part, **kwargs):
        return youtube_get(cls.url, part=part, **kwargs)

    @classmethod
    def pop_extras(cls, kwargs):
        accepted = cls.accepted
        extras = dict()
        for key in kwargs.copy():
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

    def __init__(self, kind=None, etag=None, pageInfo=None, nextPageToken=None, prevPageToken=None, items=None,
                 **kwargs):
        super(Activities, self).__init__(**kwargs)
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

    def __init__(self, kind=None, etag=None, pageInfo=None, nextPageToken=None, prevPageToken=None, items=None,
                 **kwargs):
        super(Channels, self).__init__(**kwargs)
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


class GuideCategories(Resource):
    url = GUIDE_CATEGORIES_URL

    accepted = [
        'id', 'regionCode', 'hl',
    ]

    def __init__(self, kind=None, etag=None, items=None, **kwargs):
        super(GuideCategories, self).__init__(**kwargs)
        self.kind = kind
        self.etag = etag
        self._items = items
        self.parse()

    def parse(self):
        items = self._items
        self.items = [GuideCategory(**item) for item in items]


__author__ = 'lalo'
