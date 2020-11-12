#!/bin/bash
set -e

# first version
# must run from this directory

for IN in $(find . -type f -name '*.stub.html'); do
	OUT=$(echo $IN | sed -r 's/.stub//')
	echo "*** $IN >>> $OUT"
	python build-helper.py $IN $OUT
done
