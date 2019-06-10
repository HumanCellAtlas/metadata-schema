#!/bin/sh
# Adds newly created documents to the commit.

python3 src/human_readable_json.py
git add docs/jsonBrowser/*.md