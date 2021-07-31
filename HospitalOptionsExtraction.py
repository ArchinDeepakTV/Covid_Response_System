import psycopg2

from config import config


def hospital_options():
    """ query data from the hospitals table """
    sql = "SELECT hospital_id, hospital_name FROM hospitals ORDER BY distance asc, beds, oxy_tanks"
    conn = None
    updated_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchone()
        updated_rows = cur.rowcount

        H_I_D1 = []
        HName1 = []
        H_I_D2 = []
        HName2 = []
        H_I_D3 = []
        HName3 = []
        H_I_D4 = []
        HName4 = []
        H_I_D5 = []
        HName5 = []
        for i in range(0, updated_rows):
            result = list(result)
            if i == 0:
                H_I_D1 = int(result[0])
                HName1 = str(result[1])
            if i == 1:
                H_I_D2 = int(result[0])
                HName2 = str(result[1])
            if i == 2:
                H_I_D3 = int(result[0])
                HName3 = str(result[1])
            if i == 3:
                H_I_D4 = int(result[0])
                HName4 = str(result[1])
            if i == 4:
                H_I_D5 = int(result[0])
                HName5 = str(result[1])
            result = cur.fetchone()

        print(str(H_I_D1) + '   ' + HName1)

        print(str(H_I_D2) + '   ' + HName2)

        print(str(H_I_D3) + '   ' + HName3)

        print(str(H_I_D4) + '   ' + HName4)

        print(str(H_I_D5) + '   ' + HName5)

        conn.commit()

        cur.close()
        return H_I_D1, HName1, H_I_D2, HName2, H_I_D3, HName3, H_I_D4, HName4, H_I_D5, HName5
        # MailOption(H_I_D1, HName1, H_I_D2, HName2, H_I_D3, HName3, H_I_D4, HName4, H_I_D5, HName5)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


"""if __name__ == '__main__':
    H_I_D1, HName1, H_I_D2, HName2, H_I_D3, HName3, H_I_D4, HName4, H_I_D5, HName5 = hospital_options()
    print(str(H_I_D1) + HName1 + str(H_I_D2) + HName2 + str(H_I_D3) + HName3 + str(H_I_D4) + HName4 + str(
        H_I_D5) + HName5)
"""
