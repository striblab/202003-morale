import gspread, os.path, boto3, json, tempfile, requests, shutil, cv2
from PIL import Image
from datetime import datetime
from dateutil.parser import parse
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

def shape_detection(url, type):
    if type == 'photo':
        response = requests.get(url, stream=True)
        tmp = tempfile.TemporaryFile()
        tmp = response.raw

        im = Image.open(tmp)

        if im.width > im.height:
            aspect = 'Landscape'
        elif im.height > im.width:
            aspect = 'Portrait'
        elif im.height == im.width:
            aspect = 'Landscape'

        tmp.close()

        return aspect
    elif type == 'video':
        vcap = cv2.VideoCapture(url) # 0=camera

        width  = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        if width > height:
            aspect = 'Landscape'
        elif height > width:
            aspect = 'Portrait'
        elif height == width:
            aspect = 'Landscape'

        vcap.release()
        cv2.destroyAllWindows()

        return aspect


def sheet_to_json(obj, filename):
    data_json = []
    for row in islice(obj, 1, None):
        timestamp = parse(row[1]).strftime("%B %d")
        name = row[2]
        story = row[4]
        theme = switch(row[5])

        if row[7].endswith('.jpg') or row[7].endswith('.jpeg') or row[7].endswith('.png'):
            type = 'photo'
        elif row[7].endswith('MP4') or row[7].endswith('.mp4') or row[7].endswith('.mov'):
            type = 'video'
        elif row[7].endswith('.mp3') or row[7].endswith('.wav'):
            type = 'audio'
        else:
            type = 'text'

        if type == "photo":
            asset = 'https://ststatic.stimg.co/news/projects/all/202003-morale/media/' + row[7]
        else:
            asset = 'https://static.startribune.com/news/projects/all/202003-morale/media/' + row[7]

        if type == "photo" or "video":
            shape = shape_detection(asset, type)
        else:
            shape = ''

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
                "shape": shape,
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
