#!/bin/bash

python3 crawler.py \
  --pg-address 127.0.0.1:5432 \
  --pg-login postgres/postgres \
  --redis-address 127.0.0.1:6379 \
  --redis-pass redis \
  --repo-count 1 \
  --repo-hosts gerrit,github,gitlab \
  --repo-langs go,javascript,php,python,rust,typescript
