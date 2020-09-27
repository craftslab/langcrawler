# -*- coding: utf-8 -*-

import json
import os

from langcrawler.fetcher.gerrit import Gerrit, GerritException


def test_exception():
    exception = GerritException('exception')
    assert str(exception) == 'exception'


def test_gerrit():
    gerrit = Gerrit()

    data = {
        "id": "plugins%2Fcode-owners",
        "state": "ACTIVE",
        "web_links": [
            {
                "name": "gitiles",
                "url": "https://gerrit.googlesource.com/plugins/code-owners",
                "target": "_blank"
            }
        ]
    }

    try:
        buf = gerrit._schema('plugins/code-owners', data)
        buf.dump()
    except GerritException as _:
        assert False
    else:
        assert True

    try:
        _ = gerrit._commit('plugins%2Fcode-owners')
    except GerritException as _:
        assert False
    else:
        assert True
