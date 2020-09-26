#!/bin/bash

python3 crawler.py \
    --lang-type go,javascript,php,python,rust,typescript \
    --pg-address localhost:5432 \
    --pg-login postgres/postgres \
    --repo-count 2 \
    --repo-host bitbucket,gerrit,github,gitlab
