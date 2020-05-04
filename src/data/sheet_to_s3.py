import gspread, os.path, boto3, json, tempfile, requests, shutil, cv2, re
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

def url_parse(string):
    URL_REGEX = re.compile(r'''((?:mailto:|ftp://|http://|https://)[^ <>'"{}|\\^`[\]]*)''')

    return URL_REGEX.sub(r'<a class="externalLink" href="\1">Link</a>', string)


def sheet_to_json(obj, filename):
    data_json = []
    for row in islice(obj, 1, None):
        if not row[7] and not row[8]:
            continue
        else:
            raw_timestamp = parse(row[1]).strftime("%x")
            timestamp = parse(row[1]).strftime("%B %d")
            name = row[2]
            story = url_parse(row[4])
            city = row[5]

            if row[6].endswith('.jpg') or row[6].endswith('.jpeg') or row[6].endswith('.png') or row[6].endswith('JPG') or row[6].endswith('.PNG') or row[6].endswith('.JPEG'):
                type = 'photo'
            elif row[6].endswith('MP4') or row[6].endswith('.mp4') or row[6].endswith('.mov') or row[6].endswith('.MOV'):
                type = 'video'
            elif row[6].endswith('.mp3') or row[6].endswith('.wav'):
                type = 'audio'
            else:
                type = 'text'

            if type == "photo":
                # asset = 'https://ststatic.stimg.co/news/projects/all/202003-morale/media/' + row[6]
                asset = 'https://static.startribune.com/news/projects/all/202003-morale/media/' + row[6].replace(" ", "_")
            else:
                if row[6].endswith('.mov') or row[6].endswith('.MOV'):
                    asset = 'https://static.startribune.com/news/projects/all/202003-morale/media/' + row[6][:-4] + '.mp4'
                else:
                    asset = 'https://static.startribune.com/news/projects/all/202003-morale/media/' + row[6]

            if type == "photo":
                print('fetching asset ' + asset)
                shape = shape_detection(asset, type)
            elif type == "video":
                print('fetching asset ' + asset)
                shape = shape_detection(asset, type)
            else:
                shape = shape_detection(asset, type)

            if len(story) > 250:
                long = "TRUE"
            else:
                long = "FALSE"

            publish = row[7]
            from_strib = row[9]
            url = row[17]


        if not row[7] and not row[8]:
            continue
        else:
            obj_props = {
                "raw_timestamp": raw_timestamp,
                "timestamp": timestamp,
                "name": name,
                "city": city,
                "story": story,
                "asset": asset,
                "type": type,
                "shape": shape,
                "long": long,
                "publish": publish,
                "from_strib": from_strib,
                "url": url
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
