# -*- coding: utf-8 -*-
import iso8601


class Snippet(object):
    def __init__(self, publishedAt=None, channelId=None, title=None, description=None,
                 thumbnails=None, channelTitle=None, type=None, groupId=None):
        self._publishedAt = publishedAt
        self.channelId = channelId
        self.title = title
        self.description = description
        self.thumbnails = thumbnails
        self.channelTitle = channelTitle
        self.type = type
        self.groupId = groupId
        self.parse()

    def parse(self):
        publishedAt = self._publishedAt
        if publishedAt:
            publishedAt = iso8601.parse_date(publishedAt)
            self.publishedAt = publishedAt


class ContentDetails(object):
    def __init__(self, upload=None, like=None, favorite=None, comment=None, subscription=None,
                 playlistItem=None, recommendation=None, bulletin=None, social=None, channelItem=None):
        self.upload = upload
        self.like = like
        self.favorite = favorite
        self.comment = comment
        self.subscription = subscription
        self.playlistItem = playlistItem
        self.recommendation = recommendation
        self.bulletin = bulletin
        self.social = social
        self.channelItem = channelItem


__author__ = 'lalo'
