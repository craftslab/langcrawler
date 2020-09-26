# -*- coding: utf-8 -*-

from langcrawler.fetcher.gerrit import Gerrit, GerritException


def test_exception():
    exception = GerritException('exception')
    assert str(exception) == 'exception'


def test_gerrit():
    # TODO
    pass
