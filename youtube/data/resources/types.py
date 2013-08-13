# -*- coding: utf-8 -*-
from youtube.data.resources.fields import (
    Snippet, ContentDetails, InvideoPromotion,
    BrandingSettings, Status, TopicDetails, Statistics, )
from youtube.data.utils import create_or_none


class Activity(object):
    def __init__(self, kind=None, etag=None, id=None, snippet=None, contentDetails=None):
        self.kind = kind
        self.etag = etag
        self.id = id
        self._snippet = snippet
        self._contentDetails = contentDetails
        self.parse()

    def parse(self):
        self.snippet = create_or_none(Snippet, self._snippet)
        self.contentDetails = create_or_none(ContentDetails, self._contentDetails)

    def __unicode__(self):
        return unicode(self.__str__())

    def __str__(self):
        return "Activity(kind={kind},id={id} )".format(kind=self.kind, id=self.id)

    def __repr__(self):
        return self.__str__()


class Channel(object):
    def __init__(self, kind=None, etag=None, id=None, snippet=None,
                 contentDetails=None, statistics=None, topicDetails=None,
                 status=None, brandingSettings=None, invideoPromotion=None, ):
        self.kind = kind
        self.etag = etag
        self.id = id
        self._snippet = snippet
        self._contentDetails = contentDetails
        self._statistics = statistics
        self._topicDetails = topicDetails
        self._status = status
        self._brandingSettings = brandingSettings
        self._invideoPromotion = invideoPromotion
        self.parse()

    def parse(self):
        self.snippet = create_or_none(Snippet, self._snippet)
        self.contentDetails = create_or_none(ContentDetails, self._contentDetails)
        self.statistics = create_or_none(Statistics, self._statistics)
        self.topicDetails = create_or_none(TopicDetails, self._topicDetails)
        self.status = create_or_none(Status, self._status)
        self.brandingSettings = create_or_none(BrandingSettings, self._brandingSettings)
        self.invideoPromotion = create_or_none(InvideoPromotion, self._invideoPromotion)


class GuideCategory(object):
    def __init__(self, kind=None, etag=None, id=None, snippet=None, **kwargs):
        super(GuideCategory, self).__init__(**kwargs)
        self.kind = kind
        self.etag = etag
        self.id = id
        self._snippet = snippet
        self.parse()

    def parse(self):
        self.snippet = create_or_none(Snippet, self._snippet)
__author__ = 'lalo'
