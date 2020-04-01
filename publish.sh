#!/bin/bash

# remove files directory to avoid copying directory
rm -rf ./src/data/files

# unzip static file directory
pipenv run python ./src/data/zip_to_s3.py

# sync contents of folders locally to s3
aws s3 sync ./src/data/files s3://static.startribune.com/news/projects/all/202003-morale/media/

# scrape google sheet
pipenv run python ./src/data/sheet_to_s3.py

# delete the zip file
rm ./src/data/files.zip
