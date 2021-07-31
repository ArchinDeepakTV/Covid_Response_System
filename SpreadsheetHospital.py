import gspread
import pandas as pd
import psycopg2
from oauth2client.service_account import ServiceAccountCredentials

from config import config


def id_extraction(rs):
    l = []
    for i in rs:
        # converting set to list
        k = list(i)
        # taking the first element from the list and append it to the list
        l.append(k[0])
    # Converting integer list to string list
    s = [str(i) for i in l]

    # Join list items using join()
    res = "".join(s)
    return res


def ReadSheets():
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('Keys.json', scope)

    # authorize the client sheet
    client = gspread.authorize(creds)

    # get the instance of the Spreadsheet
    sheet = client.open('Hospital_Choice')

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
    choice = int(a[2])
    # print(choice)

    res = hospital_options(choice)
    return res


def hospital_options(ID):
    """ query data from the hospitals table """
    sql = """
        SELECT "hospitals"."hospital_name" 
        FROM "hospitals" 
        WHERE "hospitals"."hospital_id" =   %s;"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, [ID])
        result = cur.fetchall()
        res = str(id_extraction(result))

        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
        return res
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


if __name__ == '__main__':
    ReadSheets()
