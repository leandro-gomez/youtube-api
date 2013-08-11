# -*- coding: utf-8 -*-
import iso8601
from youtube.data_api.utils import create_or_none


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


class Channel(object):
    def __init__(self, title=None, description=None, keywords=None, defaultTab=None,
                 trackingAnalyticsAccountId=None, moderateComments=None, showRelatedChannels=None,
                 showBrowseView=None, featuredChannelsTitle=None, featuredChannelsUrls=None,
                 unsubscribedTrailer=None, profileColor=None, ):
        self.title = title
        self.description = description
        self.keywords = keywords
        self.defaultTab = defaultTab
        self.trackingAnalyticsAccountId = trackingAnalyticsAccountId
        self.moderateComments = moderateComments
        self.showRelatedChannels = showRelatedChannels
        self.showBrowseView = showBrowseView
        self.featuredChannelsTitle = featuredChannelsTitle
        self.featuredChannelsUrls = featuredChannelsUrls
        self.unsubscribedTrailer = unsubscribedTrailer
        self.profileColor = profileColor


class HasDefaultLocalizedMixin(object):
    def __init__(self, default=None, localized=None):
        self.default = default
        self.localized = localized


class BackgroundImageUrl(HasDefaultLocalizedMixin):
    pass


class LargeBrandedBannerImageImapScript(HasDefaultLocalizedMixin):
    pass


class LargeBrandedBannerImageUrl(HasDefaultLocalizedMixin):
    pass


class SmallBrandedBannerImageImapScript(HasDefaultLocalizedMixin):
    pass


class SmallBrandedBannerImageUrl(HasDefaultLocalizedMixin):
    pass


class Hint(object):
    def __init__(self, property=None, value=None):
        self.property = property
        self.value = value

    @classmethod
    def parse(cls, elements):
        hints = []
        for hint in elements:
            hints.append(cls(**hint))
        return hints


class Image(object):
    def __init__(self, bannerImageUrl=None, bannerMobileImageUrl=None, backgroundImageUrl=None,
                 largeBrandedBannerImageImapScript=None, largeBrandedBannerImageUrl=None,
                 smallBrandedBannerImageImapScript=None, smallBrandedBannerImageUrl=None,
                 watchIconImageUrl=None, trackingImageUrl=None, bannerTabletLowImageUrl=None,
                 bannerTabletImageUrl=None, bannerTabletHdImageUrl=None, bannerTabletExtraHdImageUrl=None,
                 bannerMobileLowImageUrl=None, bannerMobileMediumHdImageUrl=None, bannerMobileHdImageUrl=None,
                 bannerMobileExtraHdImageUrl=None, bannerTvImageUrl=None, bannerExternalUrl=None, hints=None):
        self.bannerImageUrl = bannerImageUrl
        self.bannerMobileImageUrl = bannerMobileImageUrl
        self._backgroundImageUrl = backgroundImageUrl
        self._largeBrandedBannerImageImapScript = largeBrandedBannerImageImapScript
        self._largeBrandedBannerImageUrl = largeBrandedBannerImageUrl
        self._smallBrandedBannerImageImapScript = smallBrandedBannerImageImapScript
        self._smallBrandedBannerImageUrl = smallBrandedBannerImageUrl
        self.watchIconImageUrl = watchIconImageUrl
        self.trackingImageUrl = trackingImageUrl
        self.bannerTabletLowImageUrl = bannerTabletLowImageUrl
        self.bannerTabletImageUrl = bannerTabletImageUrl
        self.bannerTabletHdImageUrl = bannerTabletHdImageUrl
        self.bannerTabletExtraHdImageUrl = bannerTabletExtraHdImageUrl
        self.bannerMobileLowImageUrl = bannerMobileLowImageUrl
        self.bannerMobileMediumHdImageUrl = bannerMobileMediumHdImageUrl
        self.bannerMobileHdImageUrl = bannerMobileHdImageUrl
        self.bannerMobileExtraHdImageUrl = bannerMobileExtraHdImageUrl
        self.bannerTvImageUrl = bannerTvImageUrl
        self.bannerExternalUrl = bannerExternalUrl
        self._hints = hints
        self.parse()

    def parse(self):
        self.backgroundImageUrl = create_or_none(BackgroundImageUrl, self._backgroundImageUrl)
        self.largeBrandedBannerImageImapScript = create_or_none(LargeBrandedBannerImageImapScript,
                                                                self._largeBrandedBannerImageImapScript)
        self.largeBrandedBannerImageUrl = create_or_none(LargeBrandedBannerImageUrl, self._largeBrandedBannerImageUrl)
        self.smallBrandedBannerImageImapScript = create_or_none(SmallBrandedBannerImageImapScript,
                                                                self._smallBrandedBannerImageImapScript)
        self.smallBrandedBannerImageUrl = create_or_none(SmallBrandedBannerImageUrl, self._smallBrandedBannerImageUrl)
        self.parse_hints()

    def parse_hints(self):
        hints = self._hints
        if hints:
            self.hints = Hint.parse(hints)
        else:
            self.hints = None


class Watch(object):
    def __init__(self, textColor=None, backgroundColor=None, featuredPlaylistId=None):
        self.textColor = textColor
        self.backgroundColor = backgroundColor
        self.featuredPlaylistId = featuredPlaylistId


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


class Status(object):
    def __init__(self, privacyStatus=None, isLinked=None, ):
        self.privacyStatus = privacyStatus
        self.isLinked = isLinked


class TopicDetails(object):
    def __init__(self, topicIds=None):
        self.topicIds = topicIds


class Statistics(object):
    def __init__(self, viewCount=None, commentCount=None, subscriberCount=None, videoCount=None):
        self.viewCount = viewCount
        self.commentCount = commentCount
        self.subscriberCount = subscriberCount
        self.videoCount = videoCount


class RelatedPlaylists(object):
    def __init__(self, likes=None, favorites=None, uploads=None, watchHistory=None, watchLater=None):
        self.likes = likes
        self.favorite = favorites
        self.uploads = uploads
        self.watchHistory = watchHistory
        self.watchLater = watchLater


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
        self._resourceId = resourceId
        self.parse()

    def parse(self):
        self.resourceId = create_or_none(ResourceId, **self._resourceId)


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


class ResourceId(object):
    def __init__(self, kind=None, videoId=None, channelId=None, playlistId=None):
        self.kind = kind
        self.videoId = videoId
        self.channelId = channelId
        self.playlistId = playlistId


class PageInfo(object):
    def __init__(self, totalResults=None, resultsPerPage=None):
        self.totalResults = totalResults
        self.resultsPerPage = resultsPerPage


class Timing(object):
    def __init__(self, type=None, offsetMs=None):
        self.type = type
        self.offsetMs = offsetMs


class Position(object):
    def __init__(self, type=None, cornerPosition=None):
        self.type = type
        self.cornerPosition = cornerPosition


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
