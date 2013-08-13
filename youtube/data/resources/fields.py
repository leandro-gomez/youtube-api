# -*- coding: utf-8 -*-
import iso8601
from youtube.data.resources.nested_fields import (
    Channel, Watch, Image, Hint, Position,
    Timing, Upload, Like, Favorite,
    Subscription, Comment, PlayListItem,
    Recommendation, Bulletin, Social, ChannelItem,
    RelatedPlaylists, Thumbnail, )
from youtube.data.utils import create_or_none


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
                 playlistItem=None, recommendation=None, bulletin=None, social=None,
                 channelItem=None, relatedPlaylists=None, googlePlusUserId=None):
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
        self._relatedPlaylists = relatedPlaylists
        self.googlePlusUserId = googlePlusUserId
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
        self.relatedPlaylists = create_or_none(RelatedPlaylists, self._relatedPlaylists)


class Statistics(object):
    def __init__(self, viewCount=None, commentCount=None, subscriberCount=None, videoCount=None):
        self.viewCount = viewCount
        self.commentCount = commentCount
        self.subscriberCount = subscriberCount
        self.videoCount = videoCount


class TopicDetails(object):
    def __init__(self, topicIds=None):
        self.topicIds = topicIds


class Status(object):
    def __init__(self, privacyStatus=None, isLinked=None, ):
        self.privacyStatus = privacyStatus
        self.isLinked = isLinked


class BrandingSettings(object):
    def __init__(self, channel=None, watch=None, image=None, hints=None):
        self._channel = channel
        self._watch = watch
        self._image = image
        self._hints = hints
        self.parse()

    def parse(self):
        self.channel = create_or_none(Channel, self._channel)
        self.watch = create_or_none(Watch, self._watch)
        self.image = create_or_none(Image, self._image)
        self.parse_hints()

    def parse_hints(self):
        hints = self._hints
        if hints:
            self.hints = Hint.parse(hints)
        else:
            self.hints = None


class InvideoPromotion(object):
    def __init__(self, timing=None, position=None, items=None):
        self._timing = timing
        self._position = position
        self.items = items
        self.parse()

    def parse(self):
        self.timing = create_or_none(Timing, self._timing)
        self.position = create_or_none(Position, self._position)


__author__ = 'lalo'
