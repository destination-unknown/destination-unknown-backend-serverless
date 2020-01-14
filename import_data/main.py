from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import os.path
import pickle
import pandas as pd

import settings as stt

def read_google_sheets():
    creds = None

    service = build('sheets', 'v4', developerKey=os.environ['GOOGLE_SHEETS_API_KEY'])
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
