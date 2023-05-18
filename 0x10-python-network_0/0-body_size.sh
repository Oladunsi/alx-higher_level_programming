#!/usr/bin/env bash
# gettin the body of an http request
curl -Is "$1" | grep Content-Length | cut -f2 -d' '
