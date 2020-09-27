# -*- coding: utf-8 -*-

from langcrawler.fetcher.gitlab import GitLab, GitLabException


def test_exception():
    exception = GitLabException('exception')
    assert str(exception) == 'exception'


def test_gitlab():
    _ = GitLab()
    assert True
