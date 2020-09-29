#!/bin/bash

list="langcrawler,tests"

old=$IFS IFS=$','
for item in $list; do
  black --line-length=88 $item
  flake8 --ignore=E501,F841,W605 --max-line-length=88 $item
done
IFS=$old
