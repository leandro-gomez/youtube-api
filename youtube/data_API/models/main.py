# -*- coding: utf-8 -*-
from youtube.data_API.models.supporting import Snippet


class Activity(object):
    def __init__(self, kind=None, etag=None, id=None, snippet=None, contentDetails=None):
        self.kind = kind
        self.etag = etag
        self.id = id
        self._snippet = snippet
        self.contentDetails = contentDetails
        self.parse()

    def parse(self):
        self.snippet = Snippet(**self._snippet)

    def __unicode__(self):
        return self.kind, self.etag


__author__ = 'lalo'
