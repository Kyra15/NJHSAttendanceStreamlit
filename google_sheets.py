import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pages.student_list import LocalStorageManager
import pandas as pd


def main():
    localS = LocalStorageManager()

    scope = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file'
    ]
    file_name = '.streamlit/client_key.json'
    creds = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)
    client = gspread.authorize(creds)

    spreadsheet = client.open_by_url(localS.getItem("sheets_link"))
    worksheet = spreadsheet.get_worksheet(0)
    records_data = worksheet.get_values()

    records_df = pd.DataFrame.from_dict(records_data)

    last_col = len(records_df.columns)

    returned_table = pd.read_csv("returntable.csv")
    values_list = returned_table["Attendance"].to_list()
    values_list.insert(0, "Input date here")

    if len(values_list) < len(records_df):
        values_list += [''] * (len(records_df) - len(values_list))

    records_df.insert(last_col, "", values_list, True)

    records_data = records_df.values.tolist()

    worksheet.update("A1", records_data)
