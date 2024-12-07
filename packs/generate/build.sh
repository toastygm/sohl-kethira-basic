#!/bin/bash
for i in characters characteristics mysteries; do
    ./build-pack.sh $i
    [ $? ] || exit 1
done
