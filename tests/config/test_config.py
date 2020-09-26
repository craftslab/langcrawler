# -*- coding: utf-8 -*-

from langcrawler.config.config import Config, ConfigException


def test_config():
    config = Config()

    try:
        config.lang(' ')
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
       config.lang('foo,go')
    except ConfigException as _:
       assert True
    else:
       assert False

    try:
        config.lang('go,rust')
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
       config.postgres(' ', 'postgres/postgres')
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.postgres('127.0.0.1:5432', ' ')
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.postgres('127.0.0.1:5432', 'postgres/postgres')
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.redis(' ', 'redis')
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.redis('127.0.0.1:6379', ' ')
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.redis('127.0.0.1:6379', 'redis')
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.repo(0, 'bitbucket')
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.repo(1, ' ')
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.repo(1, 'bitbucket,foo')
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.repo(1, 'bitbucket,gerrit')
    except ConfigException as _:
        assert False
    else:
        assert True
