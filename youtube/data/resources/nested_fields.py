# -*- coding: utf-8 -*-
from youtube.data.utils import create_or_none


class BaseNestedField(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)


class Channel(BaseNestedField):
    def __init__(self, title=None, description=None, keywords=None, defaultTab=None,
                 trackingAnalyticsAccountId=None, moderateComments=None, showRelatedChannels=None,
                 showBrowseView=None, featuredChannelsTitle=None, featuredChannelsUrls=None,
                 unsubscribedTrailer=None, profileColor=None, **kwargs):
        super(Channel, self).__init__(**kwargs)
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


class HasDefaultLocalizedMixin(BaseNestedField):
    def __init__(self, default=None, localized=None, **kwargs):
        super(HasDefaultLocalizedMixin, self).__init__(**kwargs)
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


class Hint(BaseNestedField):
    def __init__(self, property=None, value=None, **kwargs):
        super(Hint, self).__init__(**kwargs)
        self.property = property
        self.value = value

    @classmethod
    def parse(cls, elements):
        hints = []
        for hint in elements:
            hints.append(cls(**hint))
        return hints


class Image(BaseNestedField):
    def __init__(self, bannerImageUrl=None, bannerMobileImageUrl=None, backgroundImageUrl=None,
                 largeBrandedBannerImageImapScript=None, largeBrandedBannerImageUrl=None,
                 smallBrandedBannerImageImapScript=None, smallBrandedBannerImageUrl=None,
                 watchIconImageUrl=None, trackingImageUrl=None, bannerTabletLowImageUrl=None,
                 bannerTabletImageUrl=None, bannerTabletHdImageUrl=None, bannerTabletExtraHdImageUrl=None,
                 bannerMobileLowImageUrl=None, bannerMobileMediumHdImageUrl=None, bannerMobileHdImageUrl=None,
                 bannerMobileExtraHdImageUrl=None, bannerTvImageUrl=None, bannerExternalUrl=None, hints=None, **kwargs):
        super(Image, self).__init__(**kwargs)
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


class Watch(BaseNestedField):
    def __init__(self, textColor=None, backgroundColor=None, featuredPlaylistId=None, **kwargs):
        super(Watch, self).__init__(**kwargs)
        self.textColor = textColor
        self.backgroundColor = backgroundColor
        self.featuredPlaylistId = featuredPlaylistId


class RelatedPlaylists(BaseNestedField):
    def __init__(self, likes=None, favorites=None, uploads=None, watchHistory=None, watchLater=None, **kwargs):
        super(RelatedPlaylists, self).__init__(**kwargs)
        self.likes = likes
        self.favorite = favorites
        self.uploads = uploads
        self.watchHistory = watchHistory
        self.watchLater = watchLater


class Thumbnail(BaseNestedField):
    def __init__(self, url=None, width=None, height=None, **kwargs):
        super(Thumbnail, self).__init__(**kwargs)
        self.url = url
        self.width = width
        self.height = height

    @classmethod
    def parse(cls, elements):
        parsed = dict()
        for k, v in elements.iteritems():
            parsed[k] = cls(**v)
        return parsed


class Upload(BaseNestedField):
    def __init__(self, videoId=None, **kwargs):
        super(Upload, self).__init__(**kwargs)
        self.videoId = videoId


class HasResourceMixin(BaseNestedField):
    def __init__(self, resourceId=None, **kwargs):
        super(HasResourceMixin, self).__init__(**kwargs)
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
    def __init__(self, resourceId=None, playlistId=None, playlistItemId=None, **kwargs):
        super(PlayListItem, self).__init__(resourceId=resourceId, **kwargs)
        self.playlistId = playlistId
        self.playlistItemId = playlistItemId


class Recommendation(HasResourceMixin):
    def __init__(self, resourceId=None, reason=None, seedResourceId=None, **kwargs):
        super(Recommendation, self).__init__(resourceId=resourceId, **kwargs)
        self.reason = reason
        self.seedResourceID = seedResourceId


class Bulletin(HasResourceMixin):
    pass


class Social(HasResourceMixin):
    def __init__(self, resourceId=None, type=None, author=None, referenceUrl=None, imageUrl=None, **kwargs):
        super(Social, self).__init__(resourceId=resourceId, **kwargs)
        self.type = type
        self.author = author
        self.referenceUrl = referenceUrl
        self.imageUrl = imageUrl


class ChannelItem(HasResourceMixin):
    pass


class ResourceId(BaseNestedField):
    def __init__(self, kind=None, videoId=None, channelId=None, playlistId=None, **kwargs):
        super(ResourceId, self).__init__(**kwargs)
        self.kind = kind
        self.videoId = videoId
        self.channelId = channelId
        self.playlistId = playlistId


class PageInfo(BaseNestedField):
    def __init__(self, totalResults=None, resultsPerPage=None, **kwargs):
        super(PageInfo, self).__init__(**kwargs)
        self.totalResults = totalResults
        self.resultsPerPage = resultsPerPage


class Timing(BaseNestedField):
    def __init__(self, type=None, offsetMs=None, **kwargs):
        super(Timing, self).__init__(**kwargs)
        self.type = type
        self.offsetMs = offsetMs


class Position(BaseNestedField):
    def __init__(self, type=None, cornerPosition=None, **kwargs):
        super(Position, self).__init__(**kwargs)
        self.type = type
        self.cornerPosition = cornerPosition


class RecordingDetails(BaseNestedField):
    def __init__(self, locationDescription=None, location=None, recordingDate=None, **kwargs):
        super(RecordingDetails, self).__init__(**kwargs)
        self.locationDescription = locationDescription
        self.recordingDate = recordingDate
        self._location = location

    def parse(self):
        self.location = create_or_none(Location, self._location)


class Location(BaseNestedField):
    def __init__(self, latitude=None, longitude=None, altitude=None, **kwargs):
        super(Location, self).__init__(**kwargs)
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude


class VideoStreams(BaseNestedField):
    def __init__(self, widthPixels=None, heightPixels=None, frameRateFps=None,
                 aspectRatio=None, codec=None, bitrateBps=None, rotation=None, vendor=None, **kwargs):
        super(VideoStreams, self).__init__(**kwargs)
        self.widthPixels = widthPixels
        self.heightPixels = heightPixels
        self.frameRateFps = frameRateFps
        self.aspectRatio = aspectRatio
        self.codec = codec
        self.bitrateBps = bitrateBps
        self.rotation = rotation
        self.vendor = vendor


class AudioStreams(BaseNestedField):
    def __init__(self, channelCount=None, codec=None, bitrateBps=None, vendor=None, **kwargs):
        super(AudioStreams, self).__init__(**kwargs)
        self.channelCount = channelCount
        self.codec = codec
        self.bitrateBps = bitrateBps
        self.vendor = vendor


class RecordingLocation(BaseNestedField):
    def __init__(self, latitude=None, longitude=None, altitude=None, **kwargs):
        super(RecordingLocation, self).__init__(**kwargs)
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude


class ProcessingProgress(BaseNestedField):
    def __init__(self, partsTotal=None, partsProcessed=None, timeLeftMs=None, **kwargs):
        super(ProcessingProgress, self).__init__(**kwargs)
        self.partsTotal = partsTotal
        self.partsProcessed = partsProcessed
        self.timeLeftMs = timeLeftMs


class TagSuggestions(BaseNestedField):
    def __init__(self, tag=None, categoryRestricts=None, **kwargs):
        super(TagSuggestions, self).__init__(**kwargs)
        self.tag = tag
        self.categoryRestricts = categoryRestricts


__author__ = 'lalo'
