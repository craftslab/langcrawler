# -*- coding: utf-8 -*-

from langcrawler.request.request import Request, RequestException


def test_request():
    try:
        _ = Request(retry=-1, timeout=None)
    except RequestException as _:
        assert True
    else:
        assert False

    try:
        _ = Request(retry=1, timeout=-1)
    except RequestException as _:
        assert True
    else:
        assert False

    url = 'https://api.github.com/search/repositories?q=archived:false+is:public+language:go+mirror:false+stars:>=1000&sort=stars&order=desc&page=1&per_page=1'

    try:
        request = Request(retry=1, timeout=None)
        request.run(url)
    except RequestException as _:
        assert False
    else:
        assert True
