#!/bin/bash

TMP_DIR=$(mktemp -d)

cp -rL homework02 "$TMP_DIR"

pushd "$TMP_DIR"

NAME="homework02/"$(od -A n -t d -N 2 /dev/urandom |tr -d ' ')
echo $NAME
docker build -f homework02/Dockerfile -t $NAME .

# Generate animals.json
docker run --rm -v $PWD:/data $NAME:latest generate_animals.py \
    --animals_save_path /data/homework02/animals.json

if [ ! -f homework02/animals.json ]; then
    echo "File not found!"
    exit -1
fi

OUTPUT=$(docker run --rm -v $PWD:/data $NAME:latest read_animals.py \
    --animals_json_path /data/homework02/animals.json)

if [ -z "$OUTPUT" ]; then
    echo "No output from running container. $OUTPUT"
    exit -1
fi

docker rmi $NAME:latest

popd
