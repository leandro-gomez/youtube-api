# -*- coding: utf-8 -*-
from resources.types import Activity, Channel, GuideCategory, PlaylistItem, Playlist, Search, Subscription
from utils import youtube_get, error_factory, create_or_none, extra_kwargs_warning
from youtube.data.resources.nested_fields import PageInfo

ACTIVITIES_URL = "https://www.googleapis.com/youtube/v3/activities/"

CHANNELS_URL = "https://www.googleapis.com/youtube/v3/channels"

GUIDE_CATEGORIES_URL = "https://www.googleapis.com/youtube/v3/guideCategories"

PLAY_LIST_ITEM_URL = "https://www.googleapis.com/youtube/v3/playlistItems"

PLAY_LIST_URL = "https://www.googleapis.com/youtube/v3/playlists"

SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

SUBSCRIPTIONS_URL = "https://www.googleapis.com/youtube/v3/subscriptions"


class Resource(object):
    """
    Abstract class of Resource YouTube Data API
    """
    accepted = []
    url = None
    item_class = None

    def __init__(self, kind=None, etag=None, items=None, **kwargs):
        self.extra = kwargs
        self.kind = kind
        self.etag = etag
        self._items = items or []
        self.parse()

    def parse(self):
        items = self._items
        self.items = [self.item_class(**item) for item in items]

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


class ResourcePageInfo(Resource):
    def __init__(self, kind=None, etag=None, pageInfo=None, nextPageToken=None,
                 prevPageToken=None, items=None, **kwargs):
        self._pageInfo = pageInfo
        self.nextPageToken = nextPageToken
        self.prevPageToken = prevPageToken
        super(ResourcePageInfo, self).__init__(kind=kind, etag=etag, items=items, **kwargs)

    def parse(self):
        self.pageInfo = create_or_none(PageInfo, self._pageInfo)
        super(ResourcePageInfo, self).parse()


class Activities(ResourcePageInfo):
    url = ACTIVITIES_URL
    item_class = Activity
    accepted = [
        'channelId', 'home', 'maxResults',
        'mine', 'pageToken', 'publishedAfter',
        'publishedBefore', 'regionCode', 'fields',
    ]


class Channels(ResourcePageInfo):
    url = CHANNELS_URL
    item_class = Channel
    accepted = [
        'categoryId', 'forUsername', 'id',
        'managedByMe', 'mine', 'mySubscribers',
        'maxResults', 'onBehalfOfContentOwner',
        'pageToken', 'fields',
    ]


class GuideCategories(Resource):
    url = GUIDE_CATEGORIES_URL
    item_class = GuideCategory
    accepted = [
        'id', 'regionCode', 'hl',
    ]


class PlaylistItems(ResourcePageInfo):
    item_class = PlaylistItem

    url = PLAY_LIST_ITEM_URL

    accepted = [
        'id', 'playlistId', 'maxResults',
        'pageToken', 'videoId',
    ]


class Playlists(ResourcePageInfo):
    item_class = Playlist
    url = PLAY_LIST_URL
    accepted = [
        'channelId', 'id', 'mine', 'maxResults', 'pageToken'
    ]


class Searches(ResourcePageInfo):
    url = SEARCH_URL
    item_class = Search
    accepted = [
        'forContentOwner', 'forMine', 'relatedToVideoId', 'channelId', 'channelType', 'maxResults',
        'onBehalfOfContentOwner', 'order', 'pageToken', 'publishedAfter', 'publishedBefore', 'q',
        'regionCode', 'safeSearch', 'topicId', 'type', 'videoCaption', 'videoCategoryId',
        'videoDefinition', 'videoDimension', 'videoDuration', 'videoEmbeddable', 'videoLicense',
        'videoSyndicated', 'videoType',
    ]


class Subscriptions(ResourcePageInfo):
    url = SUBSCRIPTIONS_URL
    item_class = Subscription
    accepted = [
        'channelId', 'id', 'mine', 'mySubscribers',
        'forChannelId', 'maxResults', 'order', 'pageToken',
    ]


__author__ = 'lalo'
