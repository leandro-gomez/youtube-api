# -*- coding: utf-8 -*-
from unittest import TestCase
from youtube.data.utils import youtube_get


VALID_RESPONSE = {
    u'items': [
        {
            u'snippet': {
                u'thumbnails': {
                    u'default': {
                        u'url': u'https://lh3.googleusercontent.com/-xIxBV3gZJqc/AAAAAAAAAAI/AAAAAAAAAAA/FSx_SCW1nr0/s88-c-k/photo.jpg'}},
                u'description': u'', u'publishedAt': u'2013-02-22T01:02:06.000Z',
                u'title': u'Leandro Gomez'
            },
            u'contentDetails': {
                u'relatedPlaylists': {
                    u'uploads': u'UUY-THBWXJ24cf-mXHr_nLYw'
                },
                u'googlePlusUserId': u'112345756060309912919'
            }, u'kind': u'youtube#channel',
            u'etag': u'"jqkgdlxEh5z8o67pDlOVdfA3-9M/Kv6YFdgwBbjfYpREXzNr39-BrM8"',
            u'id': u'UCY-THBWXJ24cf-mXHr_nLYw'
        }
    ],
    u'kind': u'youtube#channelListResponse',
    u'etag': u'"jqkgdlxEh5z8o67pDlOVdfA3-9M/d9i6Hnn14ID1Y5cXRp2eBiGwGlc"',
    u'pageInfo': {
        u'resultsPerPage': 1, u'totalResults': 1
    }
}


def get_response(*args, **kwargs):
    class A(object):
        pass

    a = A()
    a.json = lambda: VALID_RESPONSE
    return a


class UtilsTest(TestCase):
    def test_youtube_get_returns_python_dict(self):
        response = youtube_get('foo', get_method=get_response, key="bar", part="bas", id="foobar")
        self.assertEqual(response, VALID_RESPONSE)


__author__ = 'lalo'
