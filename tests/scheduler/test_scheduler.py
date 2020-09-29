# -*- coding: utf-8 -*-

from langcrawler.scheduler.scheduler import SchedulerException


def test_exception():
    exception = SchedulerException("exception")
    assert str(exception) == "exception"


def test_scheduler():
    # TODO
    pass
