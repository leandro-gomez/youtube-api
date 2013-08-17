youtube-api
===========

Python Youtube API (0.0.1)


This is an library with the intent that create a happy python YouTube API (It's just a Youtube wrapper).

OAuth 2.0 is not supported yet.

Supported data APIs:

Activity: list

Channels: list

GuideCategories: list

PlaylistItems: list

Playlists: list

Search: list

Subscriptions: list

VideoCategories: list

Videos: list


Example:

    In [1]: from data.api import Channels

    In [2]: channels_query = Channels.list(part="id,snippet,brandingSettings,contentDetails,invideoPromotion,statistics,topicDetails", id="UCY-THBWXJ24cf-mXHr_nLYw")

    In [3]: channels_query??

    Type:       Channels
    String Form:<data.api.Channels object at 0x9b20f4c>
    File:       /home/lalo/dev/python/others/youtube-api/youtube/data/api.py
    Source:
    class Channels(ResourcePageInfo):
        url = CHANNELS_URL
        item_class = Channel

    In [4]: channel  = channels_query.items[0]

    In [5]: channel?
    Type:       Channel
    String Form:Channel(kind=youtube#channel,id=UCY-THBWXJ24cf-mXHr_nLYw )
    File:       /home/lalo/dev/python/others/youtube-api/youtube/data/resources/types.py
    Docstring:  <no docstring>

    In [6]: channel.kind
    Out[6]: u'youtube#channel'

    In [7]: channel.snippet.title
    Out[9]: u'Leandro Gomez'

    In [8]: channel.snippet.publishedAt
    Out[8]: datetime.datetime(2013, 2, 22, 1, 2, 6, tzinfo=<iso8601.iso8601.Utc object at 0x9be35ac>)

    In [9]: channel.contentDetails.googlePlusUserId
    Out[9]: u'112345756060309912919'