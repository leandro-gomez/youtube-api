# -*- coding: utf-8 -*-

API_KEY = 'AIzaSyDP74ePWyfwuHfGVnZHcM4HW4hil-4VxsU'

RESOURCE_TYPES = (
    'activity', 'channel', 'guideCategory', 'playlist',
    'playlistItem', 'search result', 'subscription', 'video',
    'videoCategory',
)

SUPPORTED_OPERATIONS = (
    'list', 'insert', 'update', 'delete',
)

RESOURCE_TYPES_SUPPORT = {
    'activity': {'list': True, 'insert': True, 'update': False, 'delete': False},
    'channel': {'list': True, 'insert': False, 'update': False, 'delete': False},
    'guideCategory': {'list': True, 'insert': False, 'update': False, 'delete': False},
    'playlist': {'list': True, 'insert': True, 'update': True, 'delete': True},
    'playlistItem': {'list': True, 'insert': True, 'update': True, 'delete': True},
    'search result': {'list': True, 'insert': False, 'update': False, 'delete': False},
    'subscription': {'list': True, 'insert': False, 'update': False, 'delete': False},
    'video': {'list': True, 'insert': True, 'update': True, 'delete': True},
    'videoCategory': {'list': True, 'insert': False, 'update': False, 'delete': False},
}



__author__ = 'lalo'
