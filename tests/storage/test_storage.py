# -*- coding: utf-8 -*-

import collections

from langcrawler.config.config import Config
from langcrawler.schema.schema import Schema, schemas
from langcrawler.storage.storage import Storage, StorageException


def test_exception():
    exception = StorageException('exception')
    assert str(exception) == 'exception'


def test_storage():
    config = Config()
    storage = Storage(config)

    try:
        storage._new_db('test')
    except StorageException as _:
        assert False
    else:
        assert True

    try:
        storage._new_tbl('test', schemas)
    except StorageException as _:
        assert False
    else:
        assert True

    try:
        storage._connect_db('test')
    except StorageException as _:
        assert False
    else:
        assert True

    data = collections.OrderedDict()
    data[Schema.HOST] = 'host'
    data[Schema.REPO] = 'repo'
    data[Schema.LANGUAGE] = 'language'
    data[Schema.URL] = 'url'
    data[Schema.CLONE] = 'clone'
    data[Schema.COMMIT] = 'commit'
    data[Schema.DATE] = 'date'

    try:
        storage._insert_data(data)
    except StorageException as _:
        assert False
    else:
        assert True

    try:
        storage._close_db()
    except StorageException as _:
        assert False
    else:
        assert True
