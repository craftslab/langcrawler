# -*- coding: utf-8 -*-

from langcrawler.fetcher.gerrit import Gerrit, GerritException


def test_exception():
    exception = GerritException("exception")
    assert str(exception) == "exception"


def test_gerrit():
    data = {
        "id": "plugins%2Fcode-owners",
        "state": "ACTIVE",
        "web_links": [
            {
                "name": "gitiles",
                "url": "https://gerrit.googlesource.com/plugins/code-owners",
                "target": "_blank",
            }
        ],
    }

    try:
        gerrit = Gerrit()
    except GerritException as _:
        assert False
    else:
        assert True

    try:
        _ = gerrit._build("plugins/code-owners", data)
    except GerritException as _:
        assert False
    else:
        assert True

    try:
        _ = gerrit._commit("plugins%2Fcode-owners")
    except GerritException as _:
        assert False
    else:
        assert True
