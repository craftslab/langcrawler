# -*- coding: utf-8 -*-

class SchemaException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Schema(object):
    def __init__(self):
        self.clone = ''
        self.commit = ''
        self.date = ''
        self.host = ''
        self.language = ''
        self.repo = ''
        self.url = ''
