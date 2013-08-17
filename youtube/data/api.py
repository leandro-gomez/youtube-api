# -*- coding: utf-8 -*-
from resources.types import Activity, Channel, GuideCategory, PlaylistItem, Playlist, Search, Subscription, VideoCategory, Video
from utils import youtube_get, error_factory, create_or_none
from youtube.data.resources.nested_fields import PageInfo

ACTIVITIES_URL = "https://www.googleapis.com/youtube/v3/activities/"

CHANNELS_URL = "https://www.googleapis.com/youtube/v3/channels"

GUIDE_CATEGORIES_URL = "https://www.googleapis.com/youtube/v3/guideCategories"

PLAY_LIST_ITEM_URL = "https://www.googleapis.com/youtube/v3/playlistItems"

PLAY_LIST_URL = "https://www.googleapis.com/youtube/v3/playlists"

SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

SUBSCRIPTIONS_URL = "https://www.googleapis.com/youtube/v3/subscriptions"

VIDEO_CATEGORIES_URL = "https://www.googleapis.com/youtube/v3/videoCategories"

VIDEOS_URL = "https://www.googleapis.com/youtube/v3/videos"


class ResourceApi(object):
    """
    Abstract class of Resource YouTube Data API
    """
    url = None
    item_class = None

    def __init__(self, kind=None, etag=None, items=None, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)
        self.kind = kind
        self.etag = etag
        self._items = items or []

    def parse(self):
        items = [self.item_class(**item) for item in self._items]
        for item in items:
            item.parse()
        self.items = items
        return self

    @classmethod
    def get(cls, part, **kwargs):
        response = youtube_get(cls.url, part=part, **kwargs)
        return response.json()

    @classmethod
    def list(cls, part=('id',), **kwargs):
        part = ",".join(part)
        response = cls.get(part, **kwargs)

        if 'error' in response:
            raise error_factory(response)
        query = cls(**response)
        query.parse()
        return query


class ResourcePageInfoApi(ResourceApi):
    def __init__(self, kind=None, etag=None, pageInfo=None, nextPageToken=None,
                 prevPageToken=None, items=None, **kwargs):
        super(ResourcePageInfoApi, self).__init__(kind=kind, etag=etag, items=items, **kwargs)
        self._pageInfo = pageInfo
        self.nextPageToken = nextPageToken
        self.prevPageToken = prevPageToken

    def parse(self):
        super(ResourcePageInfoApi, self).parse()
        self.pageInfo = create_or_none(PageInfo, self._pageInfo)


class ActivityApi(ResourcePageInfoApi):
    url = ACTIVITIES_URL
    item_class = Activity


class ChannelApi(ResourcePageInfoApi):
    url = CHANNELS_URL
    item_class = Channel


class GuideCategoryApi(ResourceApi):
    url = GUIDE_CATEGORIES_URL
    item_class = GuideCategory


class PlaylistItemApi(ResourcePageInfoApi):
    item_class = PlaylistItem
    url = PLAY_LIST_ITEM_URL


class PlaylistApi(ResourcePageInfoApi):
    item_class = Playlist
    url = PLAY_LIST_URL


class SearchApi(ResourcePageInfoApi):
    url = SEARCH_URL
    item_class = Search


class SubscriptionApi(ResourcePageInfoApi):
    url = SUBSCRIPTIONS_URL
    item_class = Subscription


class VideoCategoryApi(ResourceApi):
    url = VIDEO_CATEGORIES_URL
    item_class = VideoCategory


class VideoApi(ResourcePageInfoApi):
    url = VIDEOS_URL
    item_class = Video


__author__ = 'lalo'
