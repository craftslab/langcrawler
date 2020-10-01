# -*- coding: utf-8 -*-

from langcrawler.config.config import Config, ConfigException


def test_config():
    config = Config()

    try:
        config.pg_host = ""
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.pg_host = "127.0.0.1"
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.pg_port = 0
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.pg_port = 5432
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.pg_user = ""
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.pg_user = "postgres"
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.pg_pass = ""
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.pg_pass = "postgres"
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.redis_host = ""
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.redis_host = "127.0.0.1"
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.redis_port = 0
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.redis_port = 6379
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.redis_pass = ""
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.redis_pass = "redis"
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.repo_count = 0
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.repo_count = 1
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.repo_host = []
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.repo_host = ["gerrit"]
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.repo_lang = []
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.repo_lang = ["go"]
    except ConfigException as _:
        assert False
    else:
        assert True
