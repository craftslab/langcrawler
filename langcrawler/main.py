# -*- coding: utf-8 -*-

import sys

from .cmd.argument import Argument
from .cmd.banner import BANNER
from .logger.logger import Logger


def main():
    print(BANNER)

    argument = Argument()
    arg = argument.parse(sys.argv)

    return 0
