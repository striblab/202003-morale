from zipfile import ZipFile
import os, boto3, json

with ZipFile('./src/data/files.zip', 'r') as zipObj:
    zipObj.extractall('./src/data/')
