# -*- coding: utf-8 -*-

import requests


class GerritException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Gerrit(object):
    def __init__(self, config=None):
        if config is None:
            raise GerritException('config invalid')

    def run(self):
        # TODO
        pass
