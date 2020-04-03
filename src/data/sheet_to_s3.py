import gspread, os.path, boto3, json
from datetime import datetime
from itertools import islice
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_S3_BUCKET = os.environ.get('AWS_S3_BUCKET', '')
SHEET_ID = os.environ.get('SHEET_ID', '')
KEYFILE = './src/data/' + os.environ.get('JSON_KEY', '')

def switch(i):
    switcher = {
        "Random observations":'random_obs',
        "Helping others": 'help_others',
        "Receiving help": "rec_help",
        "Needing help": "need_help",
        "Your job": "job",
        "The economy": 'economy',
        "I've been cancelled": "cancel",
        "Anxiety and worry": "anxiety",
        "Loneliness": "lonely",
        "Boredom": "bored",
        "Food and supplies": "food",
        "Sickness and healthcare": "health",
        "Other": "other"
    }
    return switcher.get(i, "")

def sheet_to_json(obj, filename):
    data_json = []
    for row in islice(obj, 1, None):
        timestamp = row[1]
        name = row[2]
        story = row[4]
        theme = switch(row[5])
        asset = 'https://static.startribune.com/news/projects/all/202003-morale/' + row[7]
        type = row[8]
        publish = row[9]
        featured = row[10]

        if not row:
            continue
        else:
            obj_props = {
                "timestamp": timestamp,
                "name": name,
                "story": story,
                "theme": theme,
                "asset": asset,
                "type": type,
                "publish": publish,
                "featured": featured
            }
            data_json.append(obj_props)

    with open(filename, 'w') as f:
        json.dump(data_json, f)

    return

# hook up gspread credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(KEYFILE, scope)
gc = gspread.authorize(credentials)

# open sheet
sheet = gc.open_by_key(SHEET_ID).get_worksheet(0)
sheet_array = sheet.get_all_values()

sheet_to_json(sheet_array, './src/data/data.json')

# push json to static
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

s3_path = 'news/projects/all/202003-morale/'
output = s3_path + 'data.json'

s3.upload_file('./src/data/data.json', AWS_S3_BUCKET, output)
