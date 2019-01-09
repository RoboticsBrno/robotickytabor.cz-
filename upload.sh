#!/usr/bin/env bash

echo "Uploading $1"
curl -sS -F "file=@$1" -F "token=$HOST_SECRET" -F "path=$1" $HOST_UPLOAD