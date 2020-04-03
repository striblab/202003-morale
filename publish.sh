#!/bin/bash

# remove files directory to avoid copying directory
rm -rf ./src/data/files

# find the inserted zip file and rename it
find ./src/data -iname \*.zip -type f -not -path "*./src/data/zips*" -exec mv {} ./src/data/files.zip \;

# unzip static file directory
pipenv run python ./src/data/zip_to_s3.py

# move new contents to media directory
cp -a ./src/data/files/. ./src/data/media

# sync contents of folders locally to s3
aws s3 sync ./src/data/media s3://static.startribune.com/news/projects/all/202003-morale/media/

# scrape google sheet
pipenv run python ./src/data/sheet_to_s3.py

# archive zip file
mv ./src/data/files.zip ./src/data/zips/files_$(date +%Y%m%d%H%M).zip
