#!/bin/bash

echo "Run FileBot on HOST !"
docker run --rm -v /media/HDD:/tmp filebot -script fn:amc --output "/tmp" --log ALL --log-file amc.log \
        --lang fr --action move --conflict override -non-strict "/tmp/DL/complete" \
        --def "movieFormat=/tmp/Movies/{n} {y}/{fn}" --def "seriesFormat=/tmp/TV Shows/{n}/{S+s}/{fn}" \
        --def excludeList=amc.txt
echo "Clean empty directories !"
find /opt/pyload/Downloads -mindepth 1 -type d -empty -delete