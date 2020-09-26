# langcrawler

[![PyPI](https://img.shields.io/pypi/v/langcrawler.svg?color=brightgreen)](https://pypi.org/project/langcrawler/)
[![Travis](https://travis-ci.com/craftslab/langcrawler.svg?branch=master)](https://travis-ci.com/craftslab/langcrawler)
[![Coverage](https://coveralls.io/repos/github/craftslab/langcrawler/badge.svg?branch=master)](https://coveralls.io/github/craftslab/langcrawler?branch=master)
[![License](https://img.shields.io/github/license/craftslab/langcrawler.svg?color=brightgreen)](https://github.com/craftslab/langcrawler/blob/master/LICENSE)



*langcrawler* is a language crawler written in Python.



## Requirement

- Python >= 3.8
- Redis >= 6.0



## Installation

### Ubuntu

```bash
apt update
apt install -y python3-dev python3-pip python3-setuptools
pip install langcrawler
```

### Windows

```
# Install Python, Microsoft Visual C++ and Windows SDK
pip install langcrawler
```



## Updating

```bash
pip install langcrawler --upgrade
```



## Running

```bash
langcrawler \
    --lang-type go,javascript,php,python,rust,typescript \
    --redis-address 127.0.0.1:6379 \
    --redis-login redis/redis \
    --repo-count 10 \
    --repo-host bitbucket,github,gitlab
```



## Usage

```bash
usage: crawler.py [-h] [-t LANG_TYPE] [-a REDIS_ADDRESS] [-l REDIS_LOGIN]
                  [-c REPO_COUNT] [-r REPO_HOST] [-v]

Language Crawler

optional arguments:
  -h, --help            show this help message and exit
  -t LANG_TYPE, --lang-type LANG_TYPE
                        language type, default:
                        go,javascript,php,python,rust,typescript
  -a REDIS_ADDRESS, --redis-address REDIS_ADDRESS
                        redis address (host:port), default: 127.0.0.1:6379
  -l REDIS_LOGIN, --redis-login REDIS_LOGIN
                        redis login (name/pass), default: redis/redis
  -c REPO_COUNT, --repo-count REPO_COUNT
                        repository count, default: 10
  -r REPO_HOST, --repo-host REPO_HOST
                        repository host, default: bitbucket,github,gitlab
  -v, --version         show program's version number and exit
```



## License

Project License can be found [here](https://github.com/craftslab/langcrawler/blob/master/LICENSE).



## Reference

- [Search on Bitbucket](https://developer.atlassian.com/server/bitbucket/reference/rest-api/)
- [Search on GitHub](https://developer.github.com/v3/search/)
- [Search on GitLab](https://docs.gitlab.com/ee/api/api_resources.html)
