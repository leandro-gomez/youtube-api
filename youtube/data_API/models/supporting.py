# -*- coding: utf-8 -*-


class Snippet(object):
    def __init__(self, publishedAt=None, channelId=None, title=None, description=None,
                 thumbnails=None, channelTitle=None, type=None, groupId=None):
        self.publishedAt = publishedAt
        self.channelId = channelId
        self.title = title
        self.description = description
        self.thumbnails = thumbnails
        self.channelTitle = channelTitle
        self.type = type
        self.groupId = groupId


__author__ = 'lalo'
