# -*- coding: utf-8 -*-
import os

API_KEY = os.environ.get('YOUTUBE_API_KEY', None)

RESOURCE_TYPES = (
    'activity', 'channel', 'guideCategory', 'playlist',
    'playlistItem', 'search result', 'subscription', 'video',
    'videoCategory',
)

__author__ = 'lalo'
