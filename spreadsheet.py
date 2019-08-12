from __future__ import print_function
from google.oauth2 import service_account
from googleapiclient.discovery import build
from pprint import pprint
from googleapiclient import discovery
# import gspread

### Set-up spreadsheet
scopes = ['https://spreadsheets.google.com/feeds']
credentials = service_account.Credentials.from_service_account_file(
    'client_secret.json')
scoped_credentials = credentials.with_scopes(
    ['https://www.spreadsheets.google.com/feeds'])
service = build('sheets', 'v4', credentials=credentials)

spreadsheet_id = '1gYgrieP-wwyfzlP0PAB9Q_woO0WsI614vAlG5F-czTA'
range_name = 'Cards'

### Call the Sheets API (sample)
# sheet = service.spreadsheets()
# result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
# values = result.get('values', [])
# print(values)

### Flashcard Methods
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

def create_set(card_info, side_info):  # params are 2D arrays to be appended to the spreadsheet
    ### Define a named range based on data
    ## Get the current size of the spreadsheet
    cards_result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range='Cards').execute() # TO-DO: use a batch get
    cards_values = cards_result.get('values', [])
    sides_result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range='Sides').execute()
    sides_values = sides_result.get('values', [])

    ## Build the request
    requests = [
        {
            "addNamedRange": {
                "namedRange": {
                    "name": card_info[0][0] + "_Cards",
                    "range": {
                        "sheetId": 1919301030,
                        "startRowIndex": len(cards_values),
                        "endRowIndex": len(card_info) + len(cards_values),
                        "startColumnIndex": 0,
                        "endColumnIndex": len(card_info[1]),
                    },
                }
            }
        },
        {
            "addNamedRange": {
                "namedRange": {
                    "name": card_info[0][0] + "_Sides",
                    "range": {
                        "sheetId": 462820485,
                        "startRowIndex": len(sides_values),
                        "endRowIndex": len(side_info) + len(sides_values),
                        "startColumnIndex": 0,
                        "endColumnIndex": len(side_info[1]),
                    },
                }
            }
        }
    ]
    body = {'requests': requests}
    response = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id,body=body).execute()

    ### Add the flashcard data
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


def build_set(set_name,card_text,side_names): # params are the info given when a set is created
    #build the side_info array
    rows, cols = (3, len(side_names))
    side_info = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if j != 1:
                side_info[i][j] = i
            else:
                side_info[i][j] = side_names[i]
    named_side_info = [[set_name]] + side_info
    card_info = [[set_name]] + card_text
    create_set(card_info, named_side_info)

### Testing
setName = 'Three'
card_text = [['side stuff','other side stuff','third side stuff'],['s1','s2','s3']]
side_names = ['side1','side2','side3']
build_set(setName,card_text,side_names)