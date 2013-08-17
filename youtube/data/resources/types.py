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
        super(Activity, self).__init__(kind=kind, etag=etag, id=id, snippet=snippet)
        self._contentDetails = contentDetails

    def parse(self):
        super(Activity, self).parse()
        self.contentDetails = create_or_none(ContentDetails, self._contentDetails)


class Channel(ResourceType):
    def __init__(self, kind=None, etag=None, id=None, snippet=None, contentDetails=None,
                 statistics=None, topicDetails=None, status=None, brandingSettings=None,
                 invideoPromotion=None, ):
        super(Channel, self).__init__(kind=kind, etag=etag, id=id, snippet=snippet)
        self._contentDetails = contentDetails
        self._statistics = statistics
        self._topicDetails = topicDetails
        self._status = status
        self._brandingSettings = brandingSettings
        self._invideoPromotion = invideoPromotion

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
        super(PlaylistItem, self).__init__(kind=kind, etag=etag, id=id, snippet=snippet)
        self._contentDetails = contentDetails
        self._status = status

    def parse(self):
        super(PlaylistItem, self).parse()
        self.contentDetails = create_or_none(ContentDetails, self._contentDetails)
        self.status = create_or_none(Status, self._status)


class Playlist(PlaylistItem):
    def __init__(self, kind=None, etag=None, id=None, snippet=None, contentDetails=None, status=None, player=None):
        super(Playlist, self).__init__(kind=kind, etag=etag, id=id,
                                       snippet=snippet, contentDetails=contentDetails,
                                       status=status)
        self._player = player

    def parse(self):
        super(Playlist, self).parse()
        self.player = create_or_none(Player, self._player)


class Search(ResourceType):
    def parse_id(self):
        self.id = create_or_none(ResourceID, self._id)


class Subscription(ResourceType):
    def __init__(self, kind=None, etag=None, id=None, snippet=None, contentDetails=None, subscriberSnippet=None):
        super(Subscription, self).__init__(kind=kind, etag=etag, id=id, snippet=snippet)
        self._contentDetails = contentDetails
        self._subscriberSnippet = subscriberSnippet

    def parse(self):
        super(Subscription, self).parse()
        self.contentDetails = create_or_none(ContentDetails, self._contentDetails)
        self.subscriberSnippet = create_or_none(SubscriberSnippet, self._subscriberSnippet)


class VideoCategory(ResourceType):
    pass

__author__ = 'lalo'
