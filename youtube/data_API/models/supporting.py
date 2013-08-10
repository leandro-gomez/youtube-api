# -*- coding: utf-8 -*-
import iso8601
from youtube.data_API.utils import create_or_none


class Snippet(object):
    def __init__(self, publishedAt=None, channelId=None, title=None, description=None,
                 thumbnails=None, channelTitle=None, type=None, groupId=None):
        self._publishedAt = publishedAt
        self.channelId = channelId
        self.title = title
        self.description = description
        self._thumbnails = thumbnails
        self.channelTitle = channelTitle
        self.type = type
        self.groupId = groupId
        self.parse()

    def parse(self):
        self.parse_publishedAt()
        self.parse_thumbnails()

    def parse_publishedAt(self):
        publishedAt = self._publishedAt
        if publishedAt:
            publishedAt = iso8601.parse_date(publishedAt)
            self.publishedAt = publishedAt

    def parse_thumbnails(self):
        thumbnails = self._thumbnails
        if thumbnails:
            self.thumbnails = Thumbnail.parse(thumbnails)


class ContentDetails(object):
    def __init__(self, upload=None, like=None, favorite=None, comment=None, subscription=None,
                 playlistItem=None, recommendation=None, bulletin=None, social=None, channelItem=None):
        self._upload = upload
        self._like = like
        self.favorite = favorite
        self.comment = comment
        self.subscription = subscription
        self.playlistItem = playlistItem
        self.recommendation = recommendation
        self.bulletin = bulletin
        self.social = social
        self.channelItem = channelItem
        self.parse()

    def parse(self):
        self.upload = create_or_none(Upload, self._upload)
        self.like= create_or_none(Like, self._like)


class Thumbnail(object):
    def __init__(self, url=None, width=None, height=None):
        self.url = url
        self.width = width
        self.height = height

    @classmethod
    def parse(cls, elements):
        parsed = dict()
        for k, v in elements.iteritems():
            parsed[k] = cls(**v)
        return parsed


class Upload(object):
    def __init__(self, videoId=None):
        self.videoId = videoId


class HasResourceMixin(object):
    def __init__(self, resourceId=None):
        self.resourceId = resourceId


class Like(HasResourceMixin):
    pass


__author__ = 'lalo'
