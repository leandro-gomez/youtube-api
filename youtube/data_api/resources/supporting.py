# -*- coding: utf-8 -*-
from youtube.data_api.utils import create_or_none


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


__author__ = 'lalo'
