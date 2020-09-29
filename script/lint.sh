#!/bin/bash

list="langcrawler,tests"

old=$IFS IFS=$','
for item in $list; do
  black $item
  flake8 $item
done
IFS=$old
