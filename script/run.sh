#!/bin/bash

python3 crawler.py \
    --pg-address localhost:5432 \
    --pg-login postgres/postgres \
    --repo-count 2 \
    --repo-hosts gerrit,github,gitlab \
    --repo-langs go,javascript,php,python,rust,typescript
