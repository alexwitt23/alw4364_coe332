#!/bin/bash

TMP_DIR=$(mktemp -d)

cp -rL homework02 "$TMP_DIR"

pushd "$TMP_DIR"

docker build -f homework02/Dockerfile -t coe332-homework02 .

# Generate animals.json
docker run --rm -v $PWD:/data coe332-homework02:latest generate_animals.py \
    --animals_save_path /data/homework02/animals.json

if [ ! -f homework02/animals.json ]; then
    echo "File not found!"
    exit -1
fi

OUTPUT=$(docker run --rm -v $PWD:/data coe332-homework02:latest read_animals.py \
    --animals_json_path /data/homework02/animals.json)

if [ -z "$OUTPUT" ]; then
    echo "No output from running container. $OUTPUT"
    exit -1
fi

popd
