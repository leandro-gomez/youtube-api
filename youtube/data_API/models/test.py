# -*- coding: utf-8 -*-
from youtube.data_API.server_responses import Activities


def test():
    response = Activities.list(part="snippet,id", channelId='UCNTbwoSMNzYhtA5SdMLJjWA')


if __name__ == "__main__":
    test()

__author__ = 'lalo'
