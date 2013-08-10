# -*- coding: utf-8 -*- 


class YouTubeError(object):
    def __init__(self, locationType=None, domain=None, message=None, reason=None, location=None):
        self.locationType = locationType
        self.domain = domain
        self.message = message
        self.reason = reason
        self.location = location


class YouTubeException(RuntimeError):
    def __init__(self, *args, **kwargs):
        code = kwargs.pop('code', None)
        message = kwargs.pop('message', None)
        errors = kwargs.pop('errors', [])
        super(YouTubeException, self).__init__(*args, **kwargs)
        self.code = code
        self.message = message
        self.errors = [YouTubeError(error) for error in errors]


__author__ = 'lalo'
