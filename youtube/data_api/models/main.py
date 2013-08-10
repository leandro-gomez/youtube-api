# -*- coding: utf-8 -*-
from youtube.data_api.models.supporting import Snippet, ContentDetails
from youtube.data_api.utils import create_or_none


class Activity(object):
    def __init__(self, kind=None, etag=None, id=None, snippet=None, contentDetails=None):
        self.kind = kind
        self.etag = etag
        self.id = id
        self._snippet = snippet
        self._contentDetails = contentDetails
        self.parse()

    def parse(self):
        self.snippet = create_or_none(Snippet, self._snippet)
        self.contentDetails = create_or_none(ContentDetails, self._contentDetails)

    def __unicode__(self):
        return unicode(self.__str__())

    def __str__(self):
        return "Activity(kind= {kind},id:= {id} )".format(kind=self.kind, id=self.id)

    def __repr__(self):
        return self.__str__()


__author__ = 'lalo'
