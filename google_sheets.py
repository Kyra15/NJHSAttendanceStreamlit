import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pages.student_list import LocalStorageManager


localS = LocalStorageManager()

scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
]
file_name = 'client_key.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)
client = gspread.authorize(creds)

sheet = client.open(localS.getItem("sheets_name")).sheet1

# basically
# i need to get the most far-left column that has 0 text in it starting after the first row
# then, ill for loop through and update all of the cells with their corresponding value of 1 or 0
# then based on that number, I'll take the entire columna dna conditional format it for green = 1 and no color = 0
# finally, i'll output the total number of people at the bottom of the page like 5 lines after the last name
# (just get the last index of the last person + 1)

