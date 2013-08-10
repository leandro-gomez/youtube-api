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
        self._favorite = favorite
        self._comment = comment
        self._subscription = subscription
        self._playlistItem = playlistItem
        self._recommendation = recommendation
        self._bulletin = bulletin
        self._social = social
        self._channelItem = channelItem
        self.parse()

    def parse(self):
        self.upload = create_or_none(Upload, self._upload)
        self.like = create_or_none(Like, self._like)
        self.favorite = create_or_none(Favorite, self._favorite)
        self.subscription = create_or_none(Subscription, self._subscription)
        self.comment = create_or_none(Comment, self._comment)
        self.playlistItem = create_or_none(PlayListItem, self._playlistItem)
        self.recommendation = create_or_none(Recommendation, self._recommendation)
        self.bulletin = create_or_none(Bulletin, self._bulletin)
        self.social = create_or_none(Social, self._social)
        self.channelItem = create_or_none(ChannelItem, self._channelItem)


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


class Favorite(HasResourceMixin):
    pass


class Subscription(HasResourceMixin):
    pass


class Comment(HasResourceMixin):
    pass


class PlayListItem(HasResourceMixin):
    def __init__(self, resourceId=None, playlistId=None, playlistItemId=None):
        super(PlayListItem, self).__init__(resourceId=resourceId)
        self.playlistId = playlistId
        self.playlistItemId = playlistItemId


class Recommendation(HasResourceMixin):
    def __init__(self, resourceId=None, reason=None, seedResourceId=None):
        super(Recommendation, self).__init__(resourceId=resourceId)
        self.reason = reason
        self.seedResourceID = seedResourceId


class Bulletin(HasResourceMixin):
    pass


class Social(HasResourceMixin):
    def __init__(self, resourceId=None, type=None, author=None, referenceUrl=None, imageUrl=None):
        super(Social, self).__init__(resourceId=resourceId)
        self.type = type
        self.author = author
        self.referenceUrl = referenceUrl
        self.imageUrl = imageUrl


class ChannelItem(HasResourceMixin):
    pass


__author__ = 'lalo'
