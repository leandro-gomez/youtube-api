# -*- coding: utf-8 -*-
import iso8601
from youtube.data.resources.nested_fields import (
    Channel, Watch, Image, Hint, Position,
    Timing, Upload, Like, Favorite,
    Subscription, Comment, PlayListItem,
    Recommendation, Bulletin, Social, ChannelItem,
    RelatedPlaylists, Thumbnail, ResourceId, VideoStreams, AudioStreams, RecordingLocation, ProcessingProgress, TagSuggestions)
from youtube.data.utils import create_or_none


class BaseField(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)


class Snippet(BaseField):
    def __init__(self, publishedAt=None, channelId=None, title=None, description=None, resourceId=None, tags=None,
                 thumbnails=None, channelTitle=None, type=None, groupId=None, playlistId=None, position=None, **kwargs):
        super(Snippet, self).__init__(**kwargs)
        self._publishedAt = publishedAt
        self.channelId = channelId
        self.title = title
        self.description = description
        self._thumbnails = thumbnails
        self.channelTitle = channelTitle
        self.type = type
        self.groupId = groupId
        self.playlistId = playlistId
        self._resourceId = resourceId
        self.position = position
        self.tags = tags
        self.parse()

    def parse(self):
        self.parse_publishedAt()
        self.parse_thumbnails()
        self.resourceId = create_or_none(ResourceId, self._resourceId)

    def parse_publishedAt(self):
        publishedAt = self._publishedAt
        if publishedAt:
            publishedAt = iso8601.parse_date(publishedAt)
            self.publishedAt = publishedAt

    def parse_thumbnails(self):
        thumbnails = self._thumbnails
        if thumbnails:
            self.thumbnails = Thumbnail.parse(thumbnails)


class ContentDetails(BaseField):
    def __init__(self, upload=None, like=None, favorite=None, comment=None, subscription=None,
                 playlistItem=None, recommendation=None, bulletin=None, social=None, itemCount=None,
                 channelItem=None, relatedPlaylists=None, googlePlusUserId=None, videoId=None,
                 startAt=None, endAt=None, note=None, **kwargs):
        super(ContentDetails, self).__init__(**kwargs)
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
        self.videoId = videoId
        self.startAt = startAt
        self.endAt = endAt
        self.note = note
        self.itemCount = itemCount
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


class Statistics(BaseField):
    def __init__(self, viewCount=None, commentCount=None, subscriberCount=None, videoCount=None, **kwargs):
        super(Statistics, self).__init__(**kwargs)
        self.viewCount = viewCount
        self.commentCount = commentCount
        self.subscriberCount = subscriberCount
        self.videoCount = videoCount


class TopicDetails(BaseField):
    def __init__(self, topicIds=None, **kwargs):
        super(TopicDetails, self).__init__(**kwargs)
        self.topicIds = topicIds


class Status(BaseField):
    def __init__(self, privacyStatus=None, isLinked=None, **kwargs):
        super(Status, self).__init__(**kwargs)
        self.privacyStatus = privacyStatus
        self.isLinked = isLinked


class BrandingSettings(BaseField):
    def __init__(self, channel=None, watch=None, image=None, hints=None, **kwargs):
        super(BrandingSettings, self).__init__(**kwargs)
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


class InvideoPromotion(BaseField):
    def __init__(self, timing=None, position=None, items=None, **kwargs):
        super(InvideoPromotion, self).__init__(**kwargs)
        self._timing = timing
        self._position = position
        self.items = items
        self.parse()

    def parse(self):
        self.timing = create_or_none(Timing, self._timing)
        self.position = create_or_none(Position, self._position)


class Player(BaseField):
    def __init__(self, embedHtml=None, **kwargs):
        super(Player, self).__init__(**kwargs)
        self.embedHtml = embedHtml


class ResourceID(BaseField):
    def __init__(self, kind=None, videoId=None, channelId=None, playlistId=None, **kwargs):
        super(ResourceID, self).__init__(**kwargs)
        self.kind = kind
        self.videoId = videoId
        self.channelId = channelId
        self.playlistId = playlistId


class SubscriberSnippet(BaseField):
    def __init__(self, title=None, description=None, channelId=None, thumbnails=None, **kwargs):
        super(SubscriberSnippet, self).__init__(**kwargs)
        self.title = title
        self.description = description
        self.channelId = channelId
        self._thumbnails = thumbnails
        self.parse()

    def parse_thumbnails(self):
        thumbnails = self._thumbnails
        if thumbnails:
            self.thumbnails = Thumbnail.parse(thumbnails)

    def parse(self):
        self.parse_thumbnails()


class FileDetails(object):
    def __init__(self, fileName=None, fileSize=None, fileType=None, container=None,
                 videoStreams=None, audioStreams=None, durationMs=None, bitrateBps=None,
                 recordingLocation=None, creationTime=None):
        self.fileName = fileName
        self.fileSize = fileSize
        self.fileType = fileType
        self.container = container
        self._videoStreams = videoStreams
        self._audioStreams = audioStreams or []
        self.durationMs = durationMs
        self.bitrateBps = bitrateBps
        self._recordingLocation = recordingLocation
        self.creationTime = creationTime

    def parse(self):
        self.videoStreams = create_or_none(VideoStreams, self._videoStreams)
        self.audioStreams = create_or_none(AudioStreams, self._audioStreams)
        self.recordingLocation = create_or_none(RecordingLocation, self._recordingLocation)


class ProcessingDetails(object):
    def __init__(self, processingStatus=None, processingProgress=None, processingFailureReason=None,
                 fileDetailsAvailability=None, processingIssuesAvailability=None, tagSuggestionsAvailability=None,
                 editorSuggestionsAvailability=None, thumbnailsAvailability=None, ):
        self.processingStatus = processingStatus
        self._processingProgress = processingProgress
        self.processingFailureReason = processingFailureReason
        self.fileDetailsAvailability = fileDetailsAvailability
        self.processingIssuesAvailability = processingIssuesAvailability
        self.tagSuggestionsAvailability = tagSuggestionsAvailability
        self.editorSuggestionsAvailability = editorSuggestionsAvailability
        self.thumbnailsAvailability = thumbnailsAvailability

    def parse(self):
        self.processingProgress = create_or_none(ProcessingProgress, self._processingProgress)


class Suggestions(object):
    def __init__(self, processingErrors=None, processingWarnings=None, processingHints=None,
                 tagSuggestions=None, editorSuggestions=None):
        self.processingErrors = processingErrors
        self.processingWarnings = processingWarnings
        self.processingHints = processingHints
        self._tagSuggestions = tagSuggestions or []
        self.editorSuggestions = editorSuggestions

    def parse(self):
        self.tagSuggestions = [TagSuggestions(**tag) for tag in self._tagSuggestions]

__author__ = 'lalo'
