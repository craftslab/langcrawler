# langcrawler

[![PyPI](https://img.shields.io/pypi/v/langcrawler.svg?color=brightgreen)](https://pypi.org/project/langcrawler/)
[![Travis](https://travis-ci.com/craftslab/langcrawler.svg?branch=master)](https://travis-ci.com/craftslab/langcrawler)
[![Coverage](https://coveralls.io/repos/github/craftslab/langcrawler/badge.svg?branch=master)](https://coveralls.io/github/craftslab/langcrawler?branch=master)
[![License](https://img.shields.io/github/license/craftslab/langcrawler.svg?color=brightgreen)](https://github.com/craftslab/langcrawler/blob/master/LICENSE)



*langcrawler* is a language crawler written in Python.



## Requirement

- PostgreSQL >= 12.4
- Python >= 3.8



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
    --pg-address localhost:5432 \
    --pg-login postgres/postgres \
    --repo-count 2 \
    --repo-host bitbucket,github,gitlab
```



## License

Project License can be found [here](https://github.com/craftslab/langcrawler/blob/master/LICENSE).



## Reference

- [Search on Bitbucket](https://developer.atlassian.com/server/bitbucket/reference/rest-api/)
- [Search on GitHub](https://developer.github.com/v3/search/)
- [Search on GitLab](https://docs.gitlab.com/ee/api/api_resources.html)
