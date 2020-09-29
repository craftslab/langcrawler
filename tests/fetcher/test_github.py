# -*- coding: utf-8 -*-

import json
import os

from langcrawler.fetcher.github import GitHub, GitHubException


def load_data(name):
    with open(name, "r") as f:
        if name.endswith(".json"):
            data = json.load(f)
        else:
            data = None

    return data


def test_exception():
    exception = GitHubException("exception")
    assert str(exception) == "exception"


def test_github():
    github = GitHub()

    data = load_data(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "../data", "go-github.json"
        )
    )
    data = data["items"][0]

    try:
        _ = github._build(data)
    except GitHubException as _:
        assert False
    else:
        assert True

    url = data["commits_url"].replace("{/sha}", "")

    try:
        _ = github._commit(url)
    except GitHubException as _:
        assert False
    else:
        assert True
