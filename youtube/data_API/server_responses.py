# -*- coding: utf-8 -*-
from youtube.data_API.models.main import Activity
from youtube.data_API.utils import youtube_get, create_error

ACTIVITY_LIST_URL = "https://www.googleapis.com/youtube/v3/activities/"


class Activities(object):
    def __init__(self, kind=None, etag=None, pageInfo=None, nextPageToken=None, prevPageToken=None, items=None):
        self.kind = kind
        self.etag = etag
        self.pageInfo = pageInfo
        self.nextPageToken = nextPageToken
        self.prevPageToken = prevPageToken
        self._items = items or []
        self.parse()

    def parse(self):
        items = self._items
        self.items = [Activity(**item) for item in items]

    @classmethod
    def list(cls, **kwargs):
        response = youtube_get(ACTIVITY_LIST_URL, **kwargs)
        if 'error' in response:
            raise create_error(response)
        return cls(**response)


__author__ = 'lalo'
