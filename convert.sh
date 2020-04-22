#!/bin/bash

FILES=./src/data/media/*

for f in $FILES
do
  mv "$f" "${f// /_}";
  if [ ${f: -4} == ".MOV" ] || [ ${f: -4} == ".mov" ]
  then
    file=${f:0:${#f}-4}".mp4"
    ffmpeg -i $f -vcodec h264 -acodec mp2 $file
  fi
done
