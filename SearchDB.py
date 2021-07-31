import psycopg2

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
    res = int("".join(s))
    return res


def read_hospital_ID(ID):
    # read number of beds available in a hospital
    sql = """
    SELECT "hospitals"."hospital_id" 
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
        res = id_extraction(result)
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
        if res == ID:
            return -1
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows

