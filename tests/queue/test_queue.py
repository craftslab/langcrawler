# -*- coding: utf-8 -*-

import collections

from langcrawler.config.config import Config
from langcrawler.schema.schema import Schema
from langcrawler.queue.queue import Queue, QueueException


def test_exception():
    exception = QueueException("exception")
    assert str(exception) == "exception"


def test_queue():
    config = Config()
    config.redis_host = "127.0.0.1"
    config.redis_port = 6379
    config.redis_pass = "redis"

    try:
        queue = Queue(config)
    except QueueException as _:
        assert False
    else:
        assert True

    try:
        queue.connect(db=15)
    except QueueException as _:
        assert False
    else:
        assert True

    name = "test"

    mapping = collections.OrderedDict()
    mapping[Schema.HOST] = "host"
    mapping[Schema.REPO] = "repo"
    mapping[Schema.LANGUAGE] = "language"
    mapping[Schema.URL] = "url"
    mapping[Schema.CLONE] = "clone"
    mapping[Schema.COMMIT] = "commit"
    mapping[Schema.DATE] = "date"

    try:
        queue.set(name, "status", "status", mapping)
    except QueueException as _:
        assert False
    else:
        assert True

    try:
        _ = queue.get(name)
    except QueueException as _:
        assert False
    else:
        assert True

    try:
        queue.delete(name)
    except QueueException as _:
        assert False
    else:
        assert True

    try:
        queue.disconnect()
    except QueueException as _:
        assert False
    else:
        assert True
