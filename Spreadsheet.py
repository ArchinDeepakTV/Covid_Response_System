import time
from decimal import *

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

from Clearing import clear
from HospitalOptionsExtraction import hospital_options
from Mail5Options import MailOption, mail_healthy
from SendMailToHospital import mail_hospitals
from SpreadsheetHospital import ReadSheets


def ReadSheet():
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('Keys.json', scope)

    # authorize the client sheet
    client = gspread.authorize(creds)

    # get the instance of the Spreadsheet
    sheet = client.open('PatientX_Vitals_Report')

    # get the first sheet of the Spreadsheet
    sheet_instance = sheet.sheet1

    # get all the records of the data
    records_data = sheet_instance.get_all_records()

    # convert the json to dataframe
    records_df = pd.DataFrame.from_dict(records_data)

    # find length (i.e., the number of rows) of the dataframe
    length = records_df.shape[0] + 1

    # extract values stored in the last row of the spreadsheet
    a = sheet_instance.row_values(length)

    # Variable Assigned
    spo2 = int(a[2])
    pulse_rate = int(a[3])
    body_temp = Decimal(a[4])
    # room_temp = int(a[5])
    # humidity = int(a[6])

    # Logic
    health_flag = Healthy(spo2, pulse_rate, body_temp)
    if health_flag == -1:
        print('Possibly Critical')
        ID1, H1, ID2, H2, ID3, H3, ID4, H4, ID5, H5 = hospital_options()
        MailOption(ID1, H1, ID2, H2, ID3, H3, ID4, H4, ID5, H5, body_temp, spo2, pulse_rate)
        clear()
        print("Waiting for 2 minutes for User's Input")
        time.sleep(120)
        clear()
        name = ReadSheets()
        mail_hospitals(body_temp, spo2, pulse_rate, name)

    elif health_flag == 1:
        print('Probably Healthy')
        mail_healthy()


def Healthy(spo2, pulse_rate, body_temp):
    health_flag = 0

    if spo2 < 94:
        health_flag = health_flag - 1
    print('spo2')

    if pulse_rate <= 60 or pulse_rate >= 100:
        health_flag = health_flag - 1
    print('pulse rate')

    if body_temp >= 37.2:
        health_flag = health_flag - 1
    print('body temp')

    if health_flag <= -1:
        return -1
    else:
        return 1


if __name__ == '__main__':
    ReadSheet()
