#!/usr/bin/env bash

curl -sS -F "file=@$1" -F "token=$HOST_SECRET" -F "path=$1" $HOST_UPLOAD