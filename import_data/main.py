from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import os.path
import pickle
import pandas as pd

import settings as stt

def read_google_sheets():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', stt.SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()

    result_properties = sheet.values().get(spreadsheetId=stt.SPREADSHEET_ID,
                                range=stt.RANGE_PROPERTIES_EXP).execute()
    _COLUMNS_PROPERTIES = result_properties['values'][0]

    data_properties = pd.DataFrame(result_properties['values'])
    data_properties.drop(data_properties.index[0], inplace=True)
    data_properties.reset_index(drop=True, inplace=True)
    data_properties.columns = _COLUMNS_PROPERTIES

    result_qa = sheet.values().get(spreadsheetId=stt.SPREADSHEET_ID,
                                range=stt.RANGE_QA_EXP).execute()
    _COLUMNS_QA = result_qa['values'][0]

    data_qa = pd.DataFrame(result_qa['values'])
    data_qa.drop(data_qa.index[0], inplace=True)
    data_qa.reset_index(drop=True, inplace=True)
    data_qa.columns = _COLUMNS_QA

    pickle.dump(data_properties, open('data_properties.pkl', 'wb'))
    pickle.dump(data_qa, open('data_qa.pkl', 'wb'))

    return data_properties, data_qa

read_google_sheets()
print('hallo')