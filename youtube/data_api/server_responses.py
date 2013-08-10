# -*- coding: utf-8 -*-
from models.main import Activity
from utils import youtube_get, create_error, create_or_none
from youtube.data_api.models.supporting import PageInfo

ACTIVITIES_URL = "https://www.googleapis.com/youtube/v3/activities/"


class Activities(object):
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

        self._pageInfo = create_or_none(PageInfo, **self._pageInfo)

    @classmethod
    def list(cls, **kwargs):
        response = youtube_get(ACTIVITIES_URL, **kwargs)
        if 'error' in response:
            raise create_error(response)
        return cls(**response)


__author__ = 'lalo'
