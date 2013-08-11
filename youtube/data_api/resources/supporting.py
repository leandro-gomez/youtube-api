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
        self.relatedPlaylists = relatedPlaylists
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
        self.backgroundImageUrl = backgroundImageUrl
        self.largeBrandedBannerImageImapScript = largeBrandedBannerImageImapScript
        self.largeBrandedBannerImageUrl = largeBrandedBannerImageUrl
        self.smallBrandedBannerImageImapScript = smallBrandedBannerImageImapScript
        self.smallBrandedBannerImageUrl = smallBrandedBannerImageUrl
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
        self.hints = hints


class Watch(object):
    def __init__(self, textColor=None, backgroundColor=None, featuredPlaylistId=None):
        self.textColor = textColor
        self.backgroundColor = backgroundColor
        self.featuredPlaylistId = featuredPlaylistId


class BrandingSettings(object):
    def __init__(self, channel=None, watch=None, image=None):
        self.channel = channel
        self.watch = watch
        self.image = image


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
        self.timing = timing
        self.position = position
        self.items = items


__author__ = 'lalo'
