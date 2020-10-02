# -*- coding: utf-8 -*-

from langcrawler.config.config import Config, ConfigException
from langcrawler.fetcher.fetcher import Fetcher, FetcherException


def test_exception():
    exception = FetcherException("exception")
    assert str(exception) == "exception"


def test_fetcher():
    config = Config()

    try:
        config.repo_count = 1
        config.repo_lang = ["go"]
        config.repo_host = ["github"]
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        fetcher = Fetcher(config)
    except FetcherException as _:
        assert False
    else:
        assert True

    try:
        fetcher.run()
    except FetcherException as _:
        assert False
    else:
        assert True
