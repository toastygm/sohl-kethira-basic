#!/bin/bash
for i in characteristics mysteries; do
    ./build-pack.sh $i
    [ $? ] || exit 1
done
for i in characters; do
    ./build-pack.sh $i
    [ $? ] || exit 1
done
