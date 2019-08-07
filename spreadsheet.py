from __future__ import print_function
from google.oauth2 import service_account
from googleapiclient.discovery import build
from pprint import pprint
from googleapiclient import discovery
# import gspread
# import google.auth
# import pickle
# import os.path
# from google_auth_oauthlib.flow import InstalledAppFlow

#credentials, project = google.auth.default(
#    scopes=['https://www.spreadsheets.google.com/feeds'])
scopes = ['https://spreadsheets.google.com/feeds']
#creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
#client = gspread.authorize(creds)

credentials = service_account.Credentials.from_service_account_file(
    'client_secret.json')

scoped_credentials = credentials.with_scopes(
    ['https://www.spreadsheets.google.com/feeds'])
service = build('sheets', 'v4', credentials=credentials)

spreadsheet_id = '1gYgrieP-wwyfzlP0PAB9Q_woO0WsI614vAlG5F-czTA'
range_name = 'Cards'

# Call the Sheets API
sheet = service.spreadsheets()
result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
values = result.get('values', [])
#print(values)

# get_set_body = {
#   "dataFilters": [
#     {
#       object(DataFilter)
#     }
#   ],
#   "includeGridData": False,
# }

def get_cards(set_id):
    range_name = set_id + "_Cards"  # gets the set based on the defined range of the set_id
    sheet = service.spreadsheets()
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    print(values)

def get_sides(set_id):
    range_name = set_id + "_Sides"  # gets the set based on the defined range of the set_id
    sheet = service.spreadsheets()
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    print(values)

def create_set(card_info, side_info):  # card and side info are 2D arrays
    body_card = {
        'values': card_info
    }
    body_side = {
        'values': side_info
    }
    result_card = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range='Cards',
        valueInputOption='USER_ENTERED', body=body_card).execute()
    result_side = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range='Sides',
        valueInputOption='USER_ENTERED', body=body_side).execute()
    #define named range based on given data

#get_sides("One")

addedCard = [['Three','$1.00','side','side'],['Three','side','side','side']]
addedSide = [['Three','1','Side 1','1'],['Three','2','Side 2','2'],['Three','3','Side 3','3']]

create_set(addedCard,addedSide)

result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
values = result.get('values', [])
pprint(values)
