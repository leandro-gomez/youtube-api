# -*- coding: utf-8 -*-
from resources.main import Activity
from utils import youtube_get, create_error, create_or_none, extra_kwargs_warning
from youtube.data_api.resources.supporting import PageInfo

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

        self.pageInfo = create_or_none(PageInfo, self._pageInfo)

    @classmethod
    def list(cls, part, channelId=None, home=None, maxResults=None,
             mine=None, pageToken=None, publishedAfter=None,
             publishedBefore=None, regionCode=None, fields=None, **kwargs):
        
        extra_kwargs_warning(kwargs)
        response = youtube_get(ACTIVITIES_URL, part=part, channelId=channelId, home=home, maxResults=maxResults,
                               mine=mine, pageToken=pageToken, publishedAfter=publishedAfter,
                               publishedBefore=publishedBefore, regionCode=regionCode, fields=fields)
        if 'error' in response:
            raise create_error(response)
        return cls(**response)


__author__ = 'lalo'
