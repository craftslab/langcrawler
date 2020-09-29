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
        config.repo_langs = ["go"]
        config.repo_hosts = ["github"]
    except ConfigException as _:
        assert False
    else:
        assert True

    fetcher = Fetcher(config)

    try:
        fetcher.run()
    except FetcherException as _:
        assert False
    else:
        assert True
