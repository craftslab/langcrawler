# -*- coding: utf-8 -*-

import argparse

from .version import VERSION


class Argument(object):
    def __init__(self):
        self._parser = argparse.ArgumentParser(description='Language Crawler')
        self._add()

    def _add(self):
        self._parser.add_argument('--lang-type',
                                  dest='lang_type',
                                  help='language type, default: go,javascript,php,python,rust,typescript',
                                  required=False)
        self._parser.add_argument('--pg-address',
                                  dest='pg_address',
                                  help='postgres address (host:port), default: 127.0.0.1:5432',
                                  required=False)
        self._parser.add_argument('--pg-login',
                                  dest='pg_login',
                                  help='postgres login (name/pass), default: postgres/postgres',
                                  required=False)
        self._parser.add_argument('--redis-address',
                                  dest='redis_address',
                                  help='redis address (host:port), default: 127.0.0.1:6379',
                                  required=False)
        self._parser.add_argument('--redis-pass',
                                  dest='redis_pass',
                                  help='redis pass, default: redis',
                                  required=False)
        self._parser.add_argument('--repo-count',
                                  dest='repo_count',
                                  help='repository count, default: 10',
                                  required=False)
        self._parser.add_argument('--repo-host',
                                  dest='repo_host',
                                  help='repository host, default: bitbucket,github,gitlab',
                                  required=False)
        self._parser.add_argument('-v', '--version',
                                  action='version',
                                  version=VERSION)

    def parse(self, argv):
        return self._parser.parse_args(argv[1:])
