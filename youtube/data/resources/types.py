# -*- coding: utf-8 -*-
from youtube.data.resources.fields import (
    Snippet, ContentDetails, InvideoPromotion,
    BrandingSettings, Status, TopicDetails, Statistics, Player, ResourceID, SubscriberSnippet)
from youtube.data.utils import create_or_none


class ResourceType(object):
    def __init__(self, kind=None, etag=None, id=None, snippet=None):
        self.kind = kind
        self.etag = etag
        self._id = id
        self._snippet = snippet
        self.parse()

    def parse(self):
        self.snippet = create_or_none(Snippet, self._snippet)
        self.parse_id()

    def parse_id(self):
        self.id = self._id

    def __unicode__(self):
        return unicode(self.__str__())

    def __str__(self):
        return "{klass}(kind={kind},id={id} )".format(klass=str(self.__class__.__name__), kind=self.kind, id=self.id)

    def __repr__(self):
        return self.__str__()


class Activity(ResourceType):
    def __init__(self, kind=None, etag=None, id=None, snippet=None, contentDetails=None):
        self._contentDetails = contentDetails
        super(Activity, self).__init__(kind=kind, etag=etag, id=id, snippet=snippet)

    def parse(self):
        super(Activity, self).parse()
        self.contentDetails = create_or_none(ContentDetails, self._contentDetails)


class Channel(ResourceType):
    def __init__(self, kind=None, etag=None, id=None, snippet=None, contentDetails=None,
                 statistics=None, topicDetails=None, status=None, brandingSettings=None,
                 invideoPromotion=None, ):
        self._contentDetails = contentDetails
        self._statistics = statistics
        self._topicDetails = topicDetails
        self._status = status
        self._brandingSettings = brandingSettings
        self._invideoPromotion = invideoPromotion
        super(Channel, self).__init__(kind=kind, etag=etag, id=id, snippet=snippet)

    def parse(self):
        super(Channel, self).parse()
        self.contentDetails = create_or_none(ContentDetails, self._contentDetails)
        self.statistics = create_or_none(Statistics, self._statistics)
        self.topicDetails = create_or_none(TopicDetails, self._topicDetails)
        self.status = create_or_none(Status, self._status)
        self.brandingSettings = create_or_none(BrandingSettings, self._brandingSettings)
        self.invideoPromotion = create_or_none(InvideoPromotion, self._invideoPromotion)


class GuideCategory(ResourceType):
    pass


class PlaylistItem(ResourceType):
    def __init__(self, kind=None, etag=None, id=None, snippet=None, contentDetails=None, status=None):
        self._contentDetails = contentDetails
        self._status = status
        super(PlaylistItem, self).__init__(kind=kind, etag=etag, id=id, snippet=snippet)

    def parse(self):
        self.contentDetails = create_or_none(ContentDetails, self._contentDetails)
        self.status = create_or_none(Status, self._status)
        super(PlaylistItem, self).parse()


class Playlist(PlaylistItem):
    def __init__(self, kind=None, etag=None, id=None, snippet=None, contentDetails=None, status=None, player=None):
        self._player = player
        super(Playlist, self).__init__(kind=kind, etag=etag, id=id,
                                       snippet=snippet, contentDetails=contentDetails,
                                       status=status)

    def parse(self):
        self.player = create_or_none(Player, self._player)
        super(Playlist, self).parse()


class Search(ResourceType):
    def parse_id(self):
        self.id = create_or_none(ResourceID, self._id)


class Subscription(ResourceType):
    def __init__(self, kind=None, etag=None, id=None, snippet=None, contentDetails=None, subscriberSnippet=None):
        self._contentDetails = contentDetails
        self._subscriberSnippet = subscriberSnippet
        super(Subscription, self).__init__(kind=kind, etag=etag, id=id, snippet=snippet)

    def parse(self):
        self.contentDetails = create_or_none(ContentDetails, self._contentDetails)
        self.subscriberSnippet = create_or_none(SubscriberSnippet, self._subscriberSnippet)
        super(Subscription, self).parse()

__author__ = 'lalo'
