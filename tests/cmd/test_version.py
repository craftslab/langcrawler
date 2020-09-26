# -*- coding: utf-8 -*-

from langcrawler.cmd.version import VERSION


def test_version():
    assert VERSION is not None and len(VERSION) != 0
