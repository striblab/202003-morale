#!/bin/bash

FILES=./src/data/media/*

for f in $FILES
do
  if [ ${f: -4} == ".MOV" ] || [ ${f: -4} == ".mov" ]
  then
    echo "mov"
  else
    echo "not mov"
  fi

done
