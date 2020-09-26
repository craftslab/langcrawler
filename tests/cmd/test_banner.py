# -*- coding: utf-8 -*-

from langcrawler.cmd.banner import BANNER


def test_banner():
    assert BANNER is not None and len(BANNER) != 0
