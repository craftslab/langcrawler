#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import setuptools

about = {}
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'langcrawler', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r') as f:
    readme = f.read()

with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]

setuptools.setup(
    author=about['__author__'],
    author_email=about['__author_email__'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    description=about['__description__'],
    download_url='https://github.com/craftslab/langcrawler/archive/v%s.tar.gz' % about['__version__'],
    entry_points={'console_scripts': ['langcrawler=langcrawler.main:main']},
    include_package_data=True,
    install_requires=requirements,
    keywords=['lang', 'language', 'crawler', 'spider'],
    license=about['__license__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    name=about['__title__'],
    packages=[about['__title__']],
    package_data={'': ['LICENSE']},
    url=about['__url__'],
    version=about['__version__'],
    zip_safe=False)
