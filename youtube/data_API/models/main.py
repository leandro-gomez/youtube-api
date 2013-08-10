# -*- coding: utf-8 -*-


class Activity(object):
    def __init__(self, kind=None, etag=None, id=None, snippet=None, contentDetails=None):
        self.kind = kind
        self.etag = etag
        self.id = id
        self.snippet = snippet
        self.contentDetails = contentDetails

    def __unicode__(self):
        return self.kind, self.etag


__author__ = 'lalo'
