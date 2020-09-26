#!/bin/bash

chmod 644 .gitignore .travis.yml
chmod 644 LICENSE MANIFEST.in README.md requirements.txt setup.cfg tox.ini
chmod 644 setup.py crawler.py

find langcrawler tests -name "*.py" -exec chmod 644 {} \;
find . -name "*.pyc" -exec rm -rf {} \;
find . -name "*.sh" -exec chmod 755 {} \;
find . -name "__pycache__" -exec rm -rf {} \;